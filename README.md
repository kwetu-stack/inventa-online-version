Inventa™ Multi-Tenant Stable v1.0
Overview
Inventa™ is a lightweight multi-tenant inventory and sales management system designed for SMEs.
This stable version (v1.0) is optimized for offline/standalone usage and serves as a backup reference for future online deployments.

The system allows real-time inventory tracking, sales recording, invoice generation (PDF + QR Code), and bulk stock import via Excel.

Features
✅ Multi-Tenant Support (Tenant Name Hardcoded for Backup Version)
✅ Dashboard: Sales charts, top-selling products, and stock overview
✅ View Products: Full inventory list with stock levels
✅ Add Stock: Update quantities instantly
✅ Record Sales: Multi-item sales recording with VAT calculations
✅ Sales History: Track all recorded sales with invoice downloads
✅ Invoice Generation: Stylish invoice with QR code
✅ Inventory Tools: Bulk upload stock data via Excel
✅ Mobile-Responsive UI
✅ Powered by Kwetu Partners Ltd

Tech Stack
Backend: Python (Flask)

Frontend: HTML, CSS (mobile responsive)

Database: SQLite (inventory.db)

Libraries:

Flask

Matplotlib

Qrcode

Pdfkit (optional, for advanced invoice exports)

Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/kwetu-stack/inventa-multitenant-stable.git
cd inventa-multitenant-stable
2. Create & Activate Virtual Environment (Windows)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
(Mac/Linux users: source venv/bin/activate)

3. Install Requirements
bash
Copy
Edit
pip install flask qrcode matplotlib pandas
4. Run the App
bash
Copy
Edit
python app.py
5. Access in Browser
cpp
Copy
Edit
http://127.0.0.1:5000
Usage
Dashboard – View sales stats and stock overview.

Inventory Tools – Download sample Excel, update stock, and re-upload.

Add Stock – Manually increase stock quantities.

Record Sales – Record transactions and auto-generate invoices.

Sales History – Download invoices in PDF.

Roadmap
v1.1 (Next) → Add Login & Tenant Authentication

v2.0 → Online multi-tenant deployment with automated onboarding.

Contributors
Kwetu Partners Ltd – Lead development

Special Thanks – Early testers and client partners

License
This project is licensed under the MIT License – free to modify and distribute.

Powered by
Kwetu Partners Ltd | www.kwetupartners.net

