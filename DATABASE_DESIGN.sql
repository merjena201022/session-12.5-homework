-- Final Schema for Book Tracker
CREATE TABLE books (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT CHECK(status IN ('want_to_read', 'reading', 'finished')),
    rating INTEGER DEFAULT 0,
    review TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);