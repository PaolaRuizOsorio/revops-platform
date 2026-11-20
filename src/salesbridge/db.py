import sqlite3
from contextlib import closing
from pathlib import Path


def init_db(db_path: Path, schema_path: Path) -> None:
    """Crea la base de datos SQLite y sus tablas a partir de un archivo SQL."""
    schema = schema_path.read_text(encoding="utf-8")
    with closing(sqlite3.connect(db_path)) as conn:
        conn.executescript(schema)
