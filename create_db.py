import sqlite3

def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()

    # Create the employee table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            pass TEXT,
            utype TEXT,
            address TEXT,
            salary TEXT
        )
    """)
    con.commit()

    # Create the supplier table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier(
            invoice TEXT PRIMARY KEY,
            name TEXT,
            contact TEXT,
            desc TEXT
        )
    """)
    con.commit()

    # Create the category table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category(
            cid TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    con.commit()

    # Create the product table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product(
            pid INTEGER PRIMARY KEY AUTOINCREMENT,
            Supplier TEXT,
            Category TEXT,
            name TEXT,
            price TEXT,
            qty TEXT,
            status TEXT
        )
    """)
    con.commit()

    con.close()

create_db()