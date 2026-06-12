import pytest
import sys
import os
import sqlite3
from flask_jwt_extended import create_access_token
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as flask_app, get_db_connection
import importlib

# Replace app.get_db_connection at import time with a test-safe wrapper that
# falls back to sqlite when the real MSSQL connection isn't available.
app_module = importlib.import_module('app')
_original_get_db = getattr(app_module, 'get_db_connection', None)
def _test_safe_get_db_connection():
    try:
        if _original_get_db:
            return _original_get_db()
    except Exception:
        pass
    # Fallback sqlite connection for tests
    sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_sqlite.db'))
    conn = sqlite3.connect(sqlite_path, check_same_thread=False)
    # Ensure tables exist
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            publisher TEXT,
            name TEXT,
            date TEXT,
            cost REAL
        )
        """
    )
    conn.commit()
    return conn

app_module.get_db_connection = _test_safe_get_db_connection

@pytest.fixture(scope="session")
def app():
    yield flask_app

@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()
    # Create a JWT directly to avoid hitting DB-backed /signup and /login endpoints.
    with flask_app.app_context():
        token = create_access_token(identity="test-user")
    client.environ_base['HTTP_AUTHORIZATION'] = f"Bearer {token}"
    return client

@pytest.fixture(scope="session")
def auth_token(client):
    """
    Creates a test user and returns a valid JWT token for the session.
    """
    # Register test user (ignore error if already exists)
    client.post("/signup", json={
        "username": "pytest_user",
        "password": "pytest_pass"
    })
    # Login and get token
    response = client.post("/login", json={
        "username": "pytest_user",
        "password": "pytest_pass"
    })
    data = response.get_json()
    return data["access_token"]

@pytest.fixture(scope="session")
def auth_headers(auth_token):
    """
    Returns headers dict with Authorization Bearer token.
    Use this in any test that calls a protected route.
    """
    return {"Authorization": f"Bearer {auth_token}"}

@pytest.fixture(scope="function")
def db_connection():
    """
    Provides a DB connection for tests. Rollback any changes after each test.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        is_sqlite = False
    except Exception:
        # Fallback to sqlite for local test runs where MSSQL is not available.
        sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_sqlite.db'))
        conn = sqlite3.connect(sqlite_path, check_same_thread=False)
        cursor = conn.cursor()
        is_sqlite = True

        # Ensure required tables exist for tests
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                publisher TEXT,
                name TEXT,
                date TEXT,
                cost REAL
            )
            """
        )
        conn.commit()
    yield conn, cursor
    conn.rollback()
    cursor.close()
    conn.close()

@pytest.fixture(scope="function")
def create_sample_book(db_connection):
    """
    Creates a sample book for testing update/delete/fetch.
    Returns the inserted book id.
    """
    conn, cursor = db_connection

    cursor.execute(
        "INSERT INTO book (publisher, name, date, cost) VALUES (?, ?, ?, ?)",
        ("TestPub", "TestBook", "2025-01-01", 50.0)
    )
    conn.commit()

    # Try MSSQL-style identity first, then fallback to DB driver's lastrowid
    book_id = None
    try:
        cursor.execute("SELECT @@IDENTITY")
        row = cursor.fetchone()
        if row:
            book_id = int(row[0])
    except Exception:
        pass

    if not book_id:
        # sqlite3 and some drivers set lastrowid on the cursor
        book_id = getattr(cursor, 'lastrowid', None)

    if not book_id:
        # Final fallback: query the max id
        cursor.execute("SELECT MAX(id) FROM book")
        book_id = int(cursor.fetchone()[0])

    yield book_id

    cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
    conn.commit()
