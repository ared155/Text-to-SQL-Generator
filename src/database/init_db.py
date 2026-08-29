import sqlite3

def init_db(db_name="demo.db"):
    # Connect to SQLite (creates file if not exists)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    );
    """)

    # Insert seed data
    cursor.executemany("INSERT INTO users (id, name, age, city) VALUES (?, ?, ?, ?);", [
        (1, 'Alice', 30, 'New York'),
        (2, 'Bob', 22, 'Chicago'),
        (3, 'Charlie', 28, 'San Francisco')
    ])

    cursor.executemany("INSERT INTO orders (id, user_id, amount, order_date) VALUES (?, ?, ?, ?);", [
        (1, 1, 1200.50, '2026-01-15'),
        (2, 2, 300.00, '2026-02-10'),
        (3, 3, 450.75, '2026-03-05')
    ])

    cursor.executemany("INSERT INTO products (id, name, price) VALUES (?, ?, ?);", [
        (1, 'Laptop', 999.99),
        (2, 'Phone', 499.99),
        (3, 'Headphones', 199.99)
    ])

    conn.commit()
    conn.close()
    print("Database initialized with tables and seed data.")

if __name__ == "__main__":
    init_db()
