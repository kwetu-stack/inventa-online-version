import sqlite3

def clear_old_sales():
    db_path = 'inventory.db'  # Make sure this matches your DB file
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM sale_items')
        cursor.execute('DELETE FROM sales')
        conn.commit()
        print("✅ Sales and sale_items tables cleared successfully.")
    except Exception as e:
        print(f"⚠️ Error clearing sales data: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    clear_old_sales()
