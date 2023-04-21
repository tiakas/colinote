import datetime
from dataclasses import dataclass


@dataclass
class Note:
    id: int
    text: str
    context: str
    created_at: datetime.datetime = datetime.datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "context": self.context,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, note_dict) -> "Note":
        return cls(
            id=note_dict["id"],
            text=note_dict["text"],
            context=note_dict["context"],
            created_at=datetime.datetime.fromisoformat(note_dict["created_at"]),
        )

    def __post_init__(self):
        self.context = self.context.strip().lower()
