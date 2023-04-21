import json
import os
from typing import List, Union

from colinote.config import data_file
from colinote.data_types import Note


def load_notes() -> List[Note]:
    """Load notes from data file"""
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            data = json.load(f)
            return [Note.from_dict(d) for d in data]
    else:
        return []


def save_notes(notes: List[Note]):
    """Save notes to data file"""
    data = [note.to_dict() for note in notes]
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)


def get_next_id(notes: List[Note]) -> int:
    """Get next available ID"""
    return max([note.id for note in notes] + [0]) + 1


def get_note_by_id(id: int, notes: List[Note]) -> Union[Note, None]:
    """Get note by ID"""
    return next((note for note in notes if note.id == id), None)


def sanitize_text(text: str) -> str:
    """Sanitize text"""
    return text.strip().lower()
