import sqlite3

# Connect to the correct database file
conn = sqlite3.connect('inventa.db')

# Create tenants table if it doesn't exist
conn.execute('''
    CREATE TABLE IF NOT EXISTS tenants (
        name TEXT PRIMARY KEY,
        is_active INTEGER NOT NULL DEFAULT 1
    )
''')

print("✅ Tenants table created.")
conn.commit()
conn.close()
