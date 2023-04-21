import json

from colinote.data_types import Note
from colinote.utils import get_next_id, get_note_by_id, load_notes

NOTES = [
    Note(
        id=1,
        text="First Message",
        context="todo",
    ),
    Note(
        id=2,
        text="Second Message",
        context="standup",
    ),
]


def test_get_next_id():
    assert get_next_id([]) == 1
    assert get_next_id(NOTES) == 3


def test_get_note_by_id():
    assert get_note_by_id(1, NOTES).context == "todo"
    assert get_note_by_id(3, NOTES) is None


def test_load_notes():
    data_file = "notes.json"
    data = [note.to_dict() for note in NOTES]
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)
    assert load_notes() == NOTES
