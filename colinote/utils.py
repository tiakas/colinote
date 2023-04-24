import json
import os
import sys
from pathlib import Path
from typing import List, Union

from colinote.data_types import Note


def default_dir() -> str:
    """Get default data file directory"""
    if sys.platform == "win32":
        config_dir = os.path.join(os.environ["APPDATA"], "colinotes")
    else:
        config_dir = os.path.join(os.path.expanduser("~"), ".config", "colinotes")
    return config_dir


def default_config() -> dict:
    """Get default configuration values"""
    config = {"file_name": "colinotes.json", "file_dir": default_dir()}
    return config


def read_config() -> dict:
    """Get configuration from config file"""
    config_file = os.path.join(default_dir(), "config.json")
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = default_config()
        write_config(config)

    return config


def write_config(config: dict) -> None:
    """
    Writes configuration to config file in default directory
    """
    config_dir = default_dir()
    config = config or default_config()

    Path(config_dir).mkdir(parents=True, exist_ok=True)
    config_file = os.path.join(config_dir, "config.json")

    with open(config_file, "w") as f:
        json.dump(config, f)


def get_data_file() -> str:
    """Get data file location"""
    config = read_config()
    return os.path.join(config["file_dir"], config["file_name"])


def load_notes() -> List[Note]:
    """Load notes from data file"""
    if os.path.exists(get_data_file()):
        with open(get_data_file(), "r") as f:
            data = json.load(f)
            return [Note.from_dict(d) for d in data]
    else:
        return []


def save_notes(notes: List[Note]):
    """Save notes to data file"""
    data = [note.to_dict() for note in notes]
    with open(get_data_file(), "w") as f:
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
