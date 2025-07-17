import sqlite3
import pandas as pd

DB_PATH = "inventory.db"

# Connect to DB
conn = sqlite3.connect(DB_PATH)

# Export Products
products = pd.read_sql_query("SELECT * FROM products", conn)
products.to_excel("digitalclub_products_backup.xlsx", index=False)

# Export Sales
sales = pd.read_sql_query("SELECT * FROM sales", conn)
sales.to_excel("digitalclub_sales_backup.xlsx", index=False)

# Export Sale Items (optional)
sale_items = pd.read_sql_query("SELECT * FROM sale_items", conn)
sale_items.to_excel("digitalclub_sale_items_backup.xlsx", index=False)

conn.close()

print("✅ Backup complete: Excel files created!")
