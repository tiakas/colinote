import itertools
from datetime import datetime
from typing import Any, List

import click
from rich.console import Console
from rich.table import Table

from colinote.data_types import Note
from colinote.utils import get_next_id, get_note_by_id, load_notes, save_notes


@click.group()
def cli():
    """
    Colinote is a command line interface for taking and managing notes.
    """
    pass


@cli.command()
@click.argument("text")
@click.option("-c", "--context", default="todo", help="Note context")
def add(text: str, context: str):
    """Add a note"""
    notes = load_notes()
    note = Note(
        id=get_next_id(notes),
        text=text,
        context=context,
    )
    notes.append(note)
    save_notes(notes)
    click.echo(f"Note {note.id} added")


@cli.command()
@click.option("-c", "--context", help="Filter notes by context")
@click.option("-d", "--date", help="Filter notes by date (YYYY-MM-DD)")
@click.option("-i", "--id", type=int, help="Get note by ID")
def show(context: str, date: str, id: int):
    """Show notes"""
    notes = load_notes()
    if id:
        filtered_notes = [note for note in notes if note.id == id]
    else:
        filtered_notes = notes
        if context:
            filtered_notes = [
                note for note in filtered_notes if note.context == context
            ]
        if date:
            filtered_notes = [
                note
                for note in filtered_notes
                if note.created_at.date() == datetime.fromisoformat(date).date()
            ]
    if filtered_notes:
        print_notes(filtered_notes)
    else:
        click.echo("No notes found")


@cli.command()
@click.argument("id", type=int)
def delete(id: int):
    """Delete a note"""
    notes = load_notes()
    for note in notes:
        if note.id == id:
            notes.remove(note)
            save_notes(notes)
            click.echo(f"Note deleted: {note}")
            break
    else:
        click.echo(f"No note found with id {id}")


@cli.command()
@click.argument("id", type=int)
@click.option("--text", "-t", type=str, default=None, help="The new text of the note")
@click.option(
    "--context",
    "-c",
    type=str,
    default=None,
    help="The new context of the note",
)
def edit(id: int, text: str, context: str):
    """Edit a note"""
    notes = load_notes()
    note = get_note_by_id(id, notes)

    if note:
        note.text = text if text else note.text
        note.context = context if context else note.context
        save_notes(notes)
        click.echo(f"Note {id} updated")
    else:
        click.echo(f"Note {id} not found")


def print_notes(notes: List[Note]):
    """Print notes to console"""
    notes = sorted(notes, key=lambda note: (note.context, note.created_at.date()))

    notes_by_context_and_date: dict[str, Any] = {}
    for (context, date), group in itertools.groupby(
        notes, key=lambda note: (note.context, note.created_at.date())
    ):
        if context not in notes_by_context_and_date:
            notes_by_context_and_date[context] = {}
        notes_by_context_and_date[context][date] = list(group)

    headers = ["Context", "Date", "ID", "Text"]
    rows = []
    for context, date_notes in notes_by_context_and_date.items():
        for date, notes in date_notes.items():
            for note in notes:
                rows.append((context, date.isoformat(), str(note.id), note.text))

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    for header in headers:
        table.add_column(header)
    for row in rows:
        table.add_row(*row)
    console.print(table)


if __name__ == "__main__":
    cli()
