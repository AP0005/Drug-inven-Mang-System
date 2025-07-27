# 💊 Drug Inventory Management System

A **Tkinter-based desktop Drug Inventory Management System** for pharmacies and hospitals. It streamlines medicinal stock control, tracks drug expiry, ensures the availability of essential medicines, and supports secure role-based access for administrators and pharmacists.

---

## 🧠 Project Description

Developed a desktop-based Drug Inventory Management System to streamline the management of medicinal stock, track drug expiry, and ensure the availability of essential drugs. The system enables real-time tracking of drug quantities, provides alerts for low stock and expiring medicines, and supports role-based access for administrators and pharmacists.

---

## 🎯 Project Motive

- Prevent drug shortages and wastage due to expiration.
- Centralize and digitize inventory records.
- Reduce human error in stock maintenance.
- Provide an offline-capable, low-cost solution for small to medium-sized clinics and pharmacies.
- Lay a foundation for scalable, automation-ready inventory systems.

---

## ✅ Features

- 🔐 **Role-based login system** (Admin and Pharmacist)
- 👩‍⚕️ **Employee Management** with full CRUD operations
- 📦 **Product Management** with expiry tracking and stock levels
- 🛒 **Supplier Management** with invoice linkage
- 🗂️ **Category Management** for logical drug grouping
- 🧾 **Sales Module** with invoice retrieval and search
- 🚨 **Low Stock and Expiry Alerts** *(enhancement ready)*
- 📊 **Dashboard overview** showing statistics for all modules
- 💾 **Data persistence** using SQLite3
- 🖥️ Fully offline, cross-platform desktop app (Windows, Linux, macOS)

---

## 🔽 Inputs & 🔼 Outputs

### Inputs:
- Employee details (Name, Email, Role, etc.)
- Supplier information (Invoice ID, Name, Contact)
- Product details (Name, Category, Supplier, Quantity, Expiry Date)
- Sales entries with invoice records

### Outputs:
- Table views with live filtering and CRUD actions
- Alert messages for success, error, and validation
- Bill files stored in `.txt` format for historical sales
- Dashboard with data metrics

---

## 📷 Screenshots

> Save your screenshots in the `assets/` folder and commit them with your repo.

| Login Page                | Dashboard                 |
|--------------------------|---------------------------|
| ![Login](assets/login.png) | ![Dashboard](assets/dashboard.png) |

| Employee Module           | Supplier Module           |
|--------------------------|---------------------------|
| ![Employee](assets/employee.png) | ![Supplier](assets/supplier.png) |

| Category Module           | Product Module            |
|--------------------------|---------------------------|
| ![Category](assets/category.png) | ![Product](assets/product.png) |

| Sales Module              |
|--------------------------|
| ![Sales](assets/sales.png) |

---

## 🗃️ Project Structure
Inventory-Management-System/
│
├── ims.db # SQLite database file
├── create_db.py # Initializes the database schema
├── login.py # Login and password verification logic
├── dashboard.py # Central GUI dashboard
├── employee.py # Employee record management
├── supplier.py # Supplier management
├── category.py # Category management
├── product.py # Product (drug) management
├── sales.py # View and search customer invoices
│
├── bill/ # Generated customer bills (.txt)
├── images/ # GUI image assets (used by Tkinter)
├── assets/ # Screenshots for README display
├── README.md # Project documentation
└── .gitignore # Files to exclude from Git



---

## 🧪 Installation & Running

### 🧰 Requirements
- Python 3.x
- Pillow (`pip install pillow`)

### 🔧 Setup Instructions

```bash
# Step 1: Clone the repository
git clone https://github.com/AP0005/Drug-inven-Mang-System
cd Drug-inven-Mang-System

# Step 2: Install dependencies
pip install pillow

# Step 3: Initialize database (Run once)
python create_db.py

# Step 4: Start the application
python login.py

