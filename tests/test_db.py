import sqlite3
from contextlib import closing
from pathlib import Path

from salesbridge.db import init_db

SCHEMA = Path(__file__).resolve().parents[1] / "sql" / "schema.sql"


def test_init_db_creates_tables(tmp_path):
    db_file = tmp_path / "test.db"

    init_db(db_file, SCHEMA)

    with closing(sqlite3.connect(db_file)) as conn:
        rows = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
    tables = {row[0] for row in rows}
    assert {"accounts", "opportunities"} <= tables
