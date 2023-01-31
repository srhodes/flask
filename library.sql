DROP DATABASE IF EXISTS library;

CREATE DATABASE library;

\c library

CREATE TABLE books
(
    id SERIAL PRIMARY KEY,
    title TEXT,
    autho TEXT,
    price FLOAT(2),
    page_count INTEGER,
    publisher TEXT,
    publication_date DATE
);