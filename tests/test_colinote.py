import json
from unittest import TestCase

from click.testing import CliRunner

from colinote.cli import add, delete, edit, show
from colinote.utils import get_data_file, write_config


class TestActions(TestCase):
    def setUp(self) -> None:
        super().setUp()
        write_config({"file_name": "notes.json", "file_dir": "."})
        self.notes_file = get_data_file()
        self.cli = CliRunner()

    def test_add(self):
        with self.cli.isolated_filesystem():
            result = self.cli.invoke(add, ["I'm the first message"])
            assert result.output == "Note 1 added\n"
            assert result.exit_code == 0
            result = self.cli.invoke(add, ["I'm the second message", "-c", "standup"])
            assert result.output == "Note 2 added\n"
            assert result.exit_code == 0

            with open(self.notes_file, "r") as f:
                data = json.load(f)
                assert len(data) == 2
                assert data[0]["id"] == 1
                assert data[0]["text"] == "I'm the first message"
                assert data[0]["context"] == "todo"
                assert data[1]["id"] == 2
                assert data[1]["text"] == "I'm the second message"
                assert data[1]["context"] == "standup"

    def test_edit(self):
        with self.cli.isolated_filesystem():
            self.cli.invoke(add, ["I'm the first message"])
            self.cli.invoke(add, ["I'm the second message", "-c", "standup"])

            result = self.cli.invoke(edit, ["1", "-t", "I'm the 1st message"])
            print(result.output)
            assert result.output == "Note 1 updated\n"
            assert result.exit_code == 0
            result = self.cli.invoke(edit, ["2", "-c", "todo"])
            assert result.output == "Note 2 updated\n"
            assert result.exit_code == 0

            with open(self.notes_file, "r") as f:
                data = json.load(f)
                assert len(data) == 2
                assert data[0]["id"] == 1
                assert data[0]["text"] == "I'm the 1st message"
                assert data[0]["context"] == "todo"
                assert data[1]["id"] == 2
                assert data[1]["text"] == "I'm the second message"
                assert data[1]["context"] == "todo"

    def test_show(self):
        with self.cli.isolated_filesystem():
            self.cli.invoke(add, ["I'm the first message"])
            self.cli.invoke(add, ["I'm the second message", "-c", "standup"])

            result = self.cli.invoke(show)
            assert result.exit_code == 0
            assert "I'm the first message" in result.output
            assert "I'm the second message" in result.output

            result = self.cli.invoke(show, ["-c", "standup"])
            assert result.exit_code == 0
            assert "I'm the first message" not in result.output
            assert "I'm the second message" in result.output

            result = self.cli.invoke(show, ["-i", "1"])
            assert result.exit_code == 0
            assert "I'm the first message" in result.output
            assert "I'm the second message" not in result.output

    def test_delete(self):
        with self.cli.isolated_filesystem():
            self.cli.invoke(add, ["I'm the first message"])

            result = self.cli.invoke(delete, ["2"])
            assert result.output == "No note found with id 2\n"

            result = self.cli.invoke(delete, ["1"])
            assert result.exit_code == 0

            with open(self.notes_file, "r") as f:
                data = json.load(f)
                assert len(data) == 0

    def test_delete_with_no_notes(self):
        with self.cli.isolated_filesystem():
            result = self.cli.invoke(delete, ["1"])
            assert result.output == "No note found with id 1\n"

    def test_delete_with_no_id(self):
        with self.cli.isolated_filesystem():
            self.cli.invoke(add, ["I'm the first message"])

            result = self.cli.invoke(delete)
            assert "Missing argument 'ID'." in result.output

    def test_delete_with_invalid_id(self):
        with self.cli.isolated_filesystem():
            self.cli.invoke(add, ["I'm the first message"])

            result = self.cli.invoke(delete, ["a"])
            assert "Invalid value for 'ID': 'a' is not a valid integer" in result.output
