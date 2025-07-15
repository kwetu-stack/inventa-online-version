# load_digital_stock.py
import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Clear old data
cursor.execute("DELETE FROM products")

# Insert dummy digital club stock
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", ("Gilbeys 750ml", 10, 950))
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", ("Chrome Vodka 250ml", 25, 320))
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", ("Kibao 750ml", 12, 580))
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", ("Tusker Cider 500ml", 30, 210))
cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", ("Summit Lager 500ml", 18, 190))

conn.commit()
conn.close()
print("✅ Dummy Digital Club stock loaded.")
