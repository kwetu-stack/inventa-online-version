import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create tenants table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tenants (
        name TEXT PRIMARY KEY,
        is_active INTEGER DEFAULT 1
    )
''')

# Remove 'alamudi' if it exists
cursor.execute('DELETE FROM tenants WHERE name = ?', ('alamudi',))

# Add active tenant for Digital Club and an inactive test client
cursor.execute('INSERT OR IGNORE INTO tenants (name, is_active) VALUES (?, ?)', ('digitalclub', 1))
cursor.execute('INSERT OR IGNORE INTO tenants (name, is_active) VALUES (?, ?)', ('testclient', 0))

conn.commit()
conn.close()

print("Alamudi removed. Tenants table updated.")
