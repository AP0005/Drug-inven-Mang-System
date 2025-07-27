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

### Login Page  ###
<img width="625" height="316" alt="login" src="https://github.com/user-attachments/assets/e0fa3629-528d-4780-8035-8df65515d50f" />

### Dashboard  ###
<img width="690" height="393" alt="dashboard" src="https://github.com/user-attachments/assets/62bb8d3f-8763-48ad-80aa-e5511b8d4301" />

### Employee Module ###
<img width="684" height="328" alt="employee" src="https://github.com/user-attachments/assets/dd8fc830-7ba9-4712-a45b-37349ef55ba1" />

### Supplier Module ###
<img width="385" height="324" alt="supplier" src="https://github.com/user-attachments/assets/1342c61d-5323-4e38-aadf-aebc6d9190b4" />

### Category Module ###
<img width="683" height="305" alt="category" src="https://github.com/user-attachments/assets/71ff3cf0-1542-4144-acdb-41b8d39afc7c" />

### Product Module  ###
<img width="683" height="338" alt="product" src="https://github.com/user-attachments/assets/51e83059-a79a-4b92-8e79-647fe30f2f6c" />

### Sales Module   ###
<img width="641" height="310" alt="sales" src="https://github.com/user-attachments/assets/a6def054-d1fe-4640-bacb-83fee8eee805" />


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

