import sqlite3

# Connect to the tenant database
conn = sqlite3.connect('../tenants/alamudi/database.db')
cur = conn.cursor()

# List all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print("Tables:", tables)

# Show all users
cur.execute("SELECT username, role FROM users")
users = cur.fetchall()
print("Users:", users)

conn.close()
