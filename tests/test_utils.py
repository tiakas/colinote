import json
from unittest import TestCase

from click.testing import CliRunner

from colinote.data_types import Note
from colinote.utils import get_next_id, get_note_by_id, load_notes, write_config

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


class TestUtils(TestCase):
    def test_get_next_id(self):
        assert get_next_id([]) == 1
        assert get_next_id(NOTES) == 3

    def test_get_note_by_id(self):
        assert get_note_by_id(1, NOTES).context == "todo"
        assert get_note_by_id(3, NOTES) is None

    def test_load_notes(self):
        write_config({"file_name": "notes.json", "file_dir": "."})
        with CliRunner().isolated_filesystem():
            data_file = "notes.json"
            data = [note.to_dict() for note in NOTES]
            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)
            assert load_notes() == NOTES
