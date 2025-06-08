import sqlite3
import os

# Ensure database directory exists
DB_PATH = os.path.join("database", "users.db")

# Initialize DB if it doesn't exist
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Register a new user
def register_user(username: str, password: str) -> tuple[bool, str]:
    """
    Registers a new user. Returns (success, message).
    """
    if not username or not password:
        return False, "Username and password cannot be empty."

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            if cursor.fetchone():
                return False, "Username already exists. Try logging in."
            
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True, "Registration successful. Please log in."
    except Exception as e:
        return False, f"Registration failed: {str(e)}"

# Validate login credentials
def validate_user(username: str, password: str) -> bool:
    """
    Validates a user's login credentials.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            return bool(cursor.fetchone())
    except Exception as e:
        print(f"Login error: {e}")
        return False

# Initialize DB on module import
init_db()
