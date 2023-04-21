import json

import pytest
from click.testing import CliRunner

from colinote.cli import add, delete, edit, show

NOTES_FILE = "notes.json"


@pytest.fixture
def runner():
    return CliRunner()


def test_add(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(add, ["I'm the first message"])
        assert result.output == "Note 1 added\n"
        assert result.exit_code == 0
        result = runner.invoke(add, ["I'm the second message", "-c", "standup"])
        assert result.output == "Note 2 added\n"
        assert result.exit_code == 0

        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
            assert len(data) == 2
            assert data[0]["id"] == 1
            assert data[0]["text"] == "I'm the first message"
            assert data[0]["context"] == "todo"
            assert data[1]["id"] == 2
            assert data[1]["text"] == "I'm the second message"
            assert data[1]["context"] == "standup"


def test_edit(runner):
    with runner.isolated_filesystem():
        runner.invoke(add, ["I'm the first message"])
        runner.invoke(add, ["I'm the second message", "-c", "standup"])

        result = runner.invoke(edit, ["1", "-t", "I'm the 1st message"])
        print(result.output)
        assert result.output == "Note 1 updated\n"
        assert result.exit_code == 0
        result = runner.invoke(edit, ["2", "-c", "todo"])
        assert result.output == "Note 2 updated\n"
        assert result.exit_code == 0

        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
            assert len(data) == 2
            assert data[0]["id"] == 1
            assert data[0]["text"] == "I'm the 1st message"
            assert data[0]["context"] == "todo"
            assert data[1]["id"] == 2
            assert data[1]["text"] == "I'm the second message"
            assert data[1]["context"] == "todo"


def test_show(runner):
    with runner.isolated_filesystem():
        runner.invoke(add, ["I'm the first message"])
        runner.invoke(add, ["I'm the second message", "-c", "standup"])

        result = runner.invoke(show)
        assert result.exit_code == 0
        assert "I'm the first message" in result.output
        assert "I'm the second message" in result.output

        result = runner.invoke(show, ["-c", "standup"])
        assert result.exit_code == 0
        assert "I'm the first message" not in result.output
        assert "I'm the second message" in result.output

        result = runner.invoke(show, ["-i", "1"])
        assert result.exit_code == 0
        assert "I'm the first message" in result.output
        assert "I'm the second message" not in result.output


def test_delete(runner):
    with runner.isolated_filesystem():
        runner.invoke(add, ["I'm the first message"])

        result = runner.invoke(delete, ["2"])
        assert result.output == "No note found with id 2\n"

        result = runner.invoke(delete, ["1"])
        assert result.exit_code == 0

        with open(NOTES_FILE, "r") as f:
            data = json.load(f)
            assert len(data) == 0
