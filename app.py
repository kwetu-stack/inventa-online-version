import os
import sqlite3
import io
from flask import Flask, render_template, request, redirect, send_file, abort, flash
import qrcode
import pandas as pd

app = Flask(__name__)
app.secret_key = 'supersecret'  # Required for flashing messages

TENANT = 'digitalclub'
DB_PATH = 'inventory.db'

# ---------- HELPER ----------
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- ROUTES ----------

@app.route('/')
def home():
    return redirect(f'/{TENANT}/dashboard')

@app.route(f'/{TENANT}/dashboard')
def dashboard():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    total_products = len(products)
    total_sales = conn.execute('SELECT SUM(grand_total) FROM sales').fetchone()[0] or 0

    sales_data = conn.execute('SELECT date, SUM(grand_total) as total FROM sales GROUP BY date ORDER BY date').fetchall()
    conn.close()

    dates = [row['date'] for row in sales_data]
    totals = [row['total'] for row in sales_data]

    return render_template(
        'dashboard.html',
        tenant=TENANT,
        total_products=total_products,
        total_sales=total_sales,
        dates=dates,
        totals=totals
    )

@app.route(f'/{TENANT}/products')
def view_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('view-products.html', products=products, tenant=TENANT)

@app.route(f'/{TENANT}/add-stock', methods=['GET', 'POST'])
def add_stock():
    conn = get_db_connection()
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        quantity = int(request.form['quantity'])

        conn.execute('UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
        conn.commit()
        conn.close()

        flash("Stock added successfully.")
        return redirect(f'/{TENANT}/add-stock')

    products = conn.execute('SELECT id, name FROM products').fetchall()
    conn.close()
    return render_template('add-stock.html', products=products, tenant=TENANT)

@app.route(f'/{TENANT}/record-sale', methods=['GET', 'POST'])
def record_sale():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()

    if request.method == 'POST':
        customer = request.form['customer']
        selected_items = []
        total_amount = 0

        product_ids = request.form.getlist('product_id[]')
        quantities = request.form.getlist('quantity[]')

        for pid, qty in zip(product_ids, quantities):
            qty = int(qty)
            if qty > 0:
                product = conn.execute('SELECT * FROM products WHERE id = ?', (pid,)).fetchone()
                subtotal = product['price'] * qty
                total_amount += subtotal
                selected_items.append((pid, qty, product['price']))

        vat = round(total_amount * 0.16, 2)
        grand_total = round(total_amount + vat, 2)

        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO sales (customer, total_amount, vat, grand_total, date) VALUES (?, ?, ?, ?, DATE("now"))',
            (customer, total_amount, vat, grand_total)
        )
        sale_id = cursor.lastrowid

        for pid, qty, price in selected_items:
            cursor.execute(
                'INSERT INTO sale_items (sale_id, product_id, quantity, price) VALUES (?, ?, ?, ?)',
                (sale_id, pid, qty, price)
            )
            cursor.execute('UPDATE products SET quantity = quantity - ? WHERE id = ?', (qty, pid))

        conn.commit()
        conn.close()
        return redirect(f'/{TENANT}/sales-history')

    conn.close()
    return render_template('record-sale.html', products=products, tenant=TENANT)

@app.route(f'/{TENANT}/sales-history')
def sales_history():
    conn = get_db_connection()
    sales = conn.execute('SELECT * FROM sales ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('sales-history.html', sales=sales, tenant=TENANT)

@app.route(f'/{TENANT}/invoice/<int:sale_id>')
def download_invoice(sale_id):
    conn = get_db_connection()
    sale = conn.execute('SELECT * FROM sales WHERE id = ?', (sale_id,)).fetchone()
    items = conn.execute('''
        SELECT p.name, si.quantity, si.price
        FROM sale_items si
        JOIN products p ON si.product_id = p.id
        WHERE si.sale_id = ?
    ''', (sale_id,)).fetchall()
    conn.close()
    return render_template('invoice.html', sale=sale, items=items, tenant=TENANT)

@app.route(f'/{TENANT}/qr/<int:sale_id>')
def generate_qr(sale_id):
    qr = qrcode.make(f"Invoice ID: {sale_id} | Tenant: {TENANT}")
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

# ---------- INVENTORY TOOLS ----------
@app.route(f'/{TENANT}/inventory-tools', methods=['GET', 'POST'])
def inventory_tools():
    if request.method == 'POST':
        file = request.files.get('excel')
        if file and file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)

            if not all(col in df.columns for col in ['Item', 'Opening stock', 'Selling price']):
                flash("Invalid file format. Ensure columns: Item, Opening stock, Selling price")
                return redirect(f'/{TENANT}/inventory-tools')

            conn = get_db_connection()
            conn.execute('DELETE FROM products')
            for _, row in df.iterrows():
                conn.execute(
                    'INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)',
                    (row['Item'], int(row['Opening stock']), float(row['Selling price']))
                )
            conn.commit()
            conn.close()
            flash("Stock imported successfully.")
            return redirect(f'/{TENANT}/inventory-tools')

    return render_template('inventory-tools.html', tenant=TENANT)

@app.route(f'/{TENANT}/download-template')
def download_template():
    df = pd.DataFrame(columns=['Item', 'Opening stock', 'Selling price'])
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='stock_template.xlsx'
    )

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
