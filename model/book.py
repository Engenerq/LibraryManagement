import json
from pathlib import Path
from dataclasses import dataclass, asdict, field
from uuid import uuid4, UUID

from custom_types.lib_db import LibDB


@dataclass
class Book:
    title: str
    author: str
    year: int
    status: bool = True
    id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, ...]:
        return asdict(self)

    def dump_file(self, path: Path) -> None:
        with (
            path.open("r", encoding="utf-8") as file_read,
            path.open("w", encoding="utf-8") as file_write,
        ):
            db: LibDB = json.load(file_read)
            db["books"].append(self.to_dict())
            json.dump(self.to_dict(), file_write, indent=4)
