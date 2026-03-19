# Inventa™ — Multi-Tenant Inventory & Sales SaaS

Inventa™ is a production-ready inventory and sales management system built to handle real-world business operations across multiple tenants.

Designed for SMEs, the platform enables efficient stock control, sales tracking, and invoice generation in a scalable, structured environment.

---

## 🚀 Overview

Inventa™ provides a complete workflow for managing inventory and sales operations:

* Real-time inventory tracking
* Multi-item sales recording with VAT calculations
* Automated invoice generation (PDF + QR Code)
* Bulk stock management via Excel import
* Multi-tenant architecture for business separation

This version represents a stable foundation for scalable SaaS deployment.

---

## 🧠 Core Features

* **Multi-Tenant Architecture** (supports multiple business environments)
* **Dashboard Analytics** (sales trends, top products, stock overview)
* **Inventory Management** (real-time stock visibility and updates)
* **Sales Processing** (multi-item transactions with automatic calculations)
* **Invoice System** (PDF invoices with embedded QR codes)
* **Sales History Tracking** (full audit trail with downloadable invoices)
* **Bulk Stock Upload** (Excel-based inventory updates)
* **Mobile-Responsive Interface**
* **Production-Oriented Design**

---

## 🛠️ Tech Stack

**Backend**

* Python (Flask)

**Frontend**

* HTML, CSS (responsive UI)

**Database**

* SQLite (local development)

**Libraries**

* Flask
* Matplotlib (analytics visualization)
* QRCode (invoice encoding)
* pdfkit (advanced PDF generation)

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/kwetu-stack/inventa-online-version.git
cd inventa-online-version
```

### 2. Create Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

*(Mac/Linux: `source venv/bin/activate`)*

### 3. Install Requirements

```bash
pip install flask qrcode matplotlib pandas pdfkit
```

### 4. Run Application

```bash
python app.py
```

### 5. Access System

```
http://127.0.0.1:5000
```

---

## 💼 Usage

* **Dashboard** → Monitor sales performance and stock levels
* **Inventory Tools** → Import/export stock using Excel
* **Add Stock** → Update inventory quantities
* **Record Sales** → Process transactions and generate invoices
* **Sales History** → Track and download past invoices

---

## 📈 Roadmap

* **v1.1** → User authentication & role-based access
* **v2.0** → Full online multi-tenant SaaS deployment
* **v2.1** → Client onboarding + billing system

---

## 👤 Author

**Bundi Murithi**
Founder & Software Engineer
Kwetu Partners Ltd

---

## 📄 License

MIT License — Free to use, modify, and distribute.

---

## 🌐 Powered by

Kwetu Partners Ltd
https://kwetupartners.net/


