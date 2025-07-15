import sqlite3

# Connect to the inventory database (will create it if it doesn't exist)
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create the tenants table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tenants (
    name TEXT PRIMARY KEY,
    is_active INTEGER DEFAULT 1
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("✅ Tenants table created successfully.")
