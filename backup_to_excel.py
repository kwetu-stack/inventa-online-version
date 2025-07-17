import sqlite3
from openpyxl import Workbook
import os
from datetime import datetime

DB_PATH = "inventory.db"
BACKUP_FOLDER = "backups"

def export_table_to_excel(table_name):
    """Exports a single table from the database to an Excel file."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        # Create a workbook
        wb = Workbook()
        ws = wb.active
        ws.title = table_name

        # Write column headers
        ws.append(columns)

        # Write data rows
        for row in rows:
            ws.append(row)

        # Ensure backup folder exists
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)

        # Add timestamp to file for versioning
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(BACKUP_FOLDER, f"{table_name}_backup_{timestamp}.xlsx")
        wb.save(file_path)

        print(f"✅ Backup complete for {table_name}: {file_path}")

    except Exception as e:
        print(f"❌ Error backing up {table_name}: {e}")
    finally:
        conn.close()

def backup_all():
    """Backs up all key tables."""
    tables = ["products", "sales", "users"]  # Add or remove table names as needed
    for table in tables:
        export_table_to_excel(table)

if __name__ == "__main__":
    backup_all()
