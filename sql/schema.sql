CREATE TABLE IF NOT EXISTS accounts (
    id        TEXT PRIMARY KEY,
    name      TEXT NOT NULL,
    type      TEXT,
    industry  TEXT
);

CREATE TABLE IF NOT EXISTS opportunities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    account_id TEXT,
    stage TEXT NOT NULL,
    close_date TEXT NOT NULL,
    amount NUMERIC,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);