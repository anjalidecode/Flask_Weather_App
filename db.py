import sqlite3
from datetime import datetime, timedelta

DB_NAME = "weather.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()

    # Table for searched cities
    conn.execute('''
        CREATE TABLE IF NOT EXISTS searched_cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            description TEXT,
            icon TEXT,
            fetched_at TIMESTAMP
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS added_cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            description TEXT,
            icon TEXT,
            fetched_at TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def get_cached_weather(city, table, cache_minutes=30):
    """Get weather from a specific table if it's recent enough."""
    conn = get_db_connection()
    result = conn.execute(
        f"SELECT * FROM {table} WHERE city = ? ORDER BY fetched_at DESC LIMIT 1",
        (city.lower(),)
    ).fetchone()
    conn.close()

    if result:
        fetched_time = datetime.fromisoformat(result["fetched_at"])
        if datetime.now() - fetched_time < timedelta(minutes=cache_minutes):
            return dict(result)
    return None

def save_weather(city, temperature, description, icon, table):
    conn = get_db_connection()
    conn.execute(
        f"INSERT INTO {table} (city, temperature, description, icon, fetched_at) VALUES (?, ?, ?, ?, ?)",
        (city.lower(), temperature, description, icon, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


