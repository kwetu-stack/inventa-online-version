import sqlite3

DB_PATH = "inventory.db"

def migrate_buying_price():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ✅ Check existing columns
    columns = [col[1] for col in cursor.execute("PRAGMA table_info(products)").fetchall()]

    # ✅ Add column if it doesn't exist
    if "buying_price" not in columns:
        cursor.execute("ALTER TABLE products ADD COLUMN buying_price REAL DEFAULT 0")
        conn.commit()
        print("✅ 'buying_price' column added successfully.")
    else:
        print("ℹ️ 'buying_price' column already exists.")

    # ✅ Populate default values (70% of selling price)
    cursor.execute("UPDATE products SET buying_price = price * 0.7 WHERE buying_price = 0")
    conn.commit()

    conn.close()
    print("✅ Buying prices updated (default: 70% of selling price).")

if __name__ == "__main__":
    migrate_buying_price()
