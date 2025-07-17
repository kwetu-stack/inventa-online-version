import sqlite3
from openpyxl import Workbook
import os

DB_PATH = "inventory.db"
BACKUP_FOLDER = "backups"

def export_table_to_excel(table_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

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

    file_path = os.path.join(BACKUP_FOLDER, f"{table_name}_backup.xlsx")
    wb.save(file_path)
    conn.close()

    print(f"✅ Backup complete for {table_name}: {file_path}")

def backup_all():
    tables = ["products", "sales", "users"]  # Adjust table names as needed
    for table in tables:
        export_table_to_excel(table)

if __name__ == "__main__":
    backup_all()
