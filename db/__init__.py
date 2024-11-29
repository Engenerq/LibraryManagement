from pathlib import Path

db = Path(__file__).parent.joinpath("db.json")

__all__ = ["db"]
