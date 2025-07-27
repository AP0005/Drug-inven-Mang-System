import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by: Shreya Sinha")
        self.root.config(bg="white")
        self.root.focus_force()

        # === All Variables ===
        self.var_searchtxt = tk.StringVar()
        self.var_sup_invoice = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_contact = tk.StringVar()

        # === Search Frame ===
        lbl_search = tk.Label(self.root, text="Invoice No.", bg="white", font=("goudy old style", 15))
        lbl_search.place(x=700, y=80)

        txt_search = tk.Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=800, y=80, width=170)

        btn_search = tk.Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"),
                               bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=980, y=79, width=100, height=28)

        # === Title ===
        title = tk.Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"),
                         bg="#1167b1", fg="white")
        title.place(x=50, y=10, width=1000, height=40)

        # === Content ===
        lbl_supplier_invoice = tk.Label(self.root, text="Invoice No", font=("goudy old style", 20), bg="white")
        lbl_supplier_invoice.place(x=50, y=80)
        txt_supplier_invoice = tk.Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 20),
                                        bg="lightyellow")
        txt_supplier_invoice.place(x=180, y=80, width=180)

        lbl_name = tk.Label(self.root, text="Name", font=("goudy old style", 20), bg="white")
        lbl_name.place(x=50, y=120)
        txt_name = tk.Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20), bg="lightyellow")
        txt_name.place(x=180, y=120, width=180)

        lbl_contact = tk.Label(self.root, text="Contact", font=("goudy old style", 20), bg="white")
        lbl_contact.place(x=50, y=160)
        txt_contact = tk.Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 20), bg="lightyellow")
        txt_contact.place(x=180, y=160, width=180)

        lbl_desc = tk.Label(self.root, text="Description", font=("goudy old style", 20), bg="white")
        lbl_desc.place(x=50, y=200)
        self.txt_desc = tk.Text(self.root, font=("goudy old style", 20), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height=80)

        # === Buttons ===
        btn_add = tk.Button(self.root, text="Save", command=self.add, font=("goudy old style", 15),
                            bg="#2196f3", fg="white", cursor="hand2")
        btn_add.place(x=180, y=320, width=110, height=35)

        btn_update = tk.Button(self.root, text="Update", command=self.update, font=("goudy old style", 15),
                               bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=300, y=320, width=110, height=35)

        btn_delete = tk.Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15),
                               bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=420, y=320, width=110, height=35)

        btn_clear = tk.Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15),
                              bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=540, y=320, width=110, height=35)

        # === Supplier Details Table ===
        emp_frame = tk.Frame(self.root, bd=3, relief="ridge")
        emp_frame.place(x=700, y=120, width=380, height=350)

        scrolly = tk.Scrollbar(emp_frame, orient=tk.VERTICAL)
        scrollx = tk.Scrollbar(emp_frame, orient=tk.HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.supplierTable.heading("invoice", text="Invoice No")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)

        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.pack(fill=tk.BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # === Functions ===
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "" or self.var_name.get() == "" or self.var_contact.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Invoice Number already assigned, try another", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)",
                                (self.var_sup_invoice.get(), self.var_name.get(), self.var_contact.get(),
                                 self.txt_desc.get('1.0', tk.END).strip()))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT invoice, name, contact, desc FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert("", tk.END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']
        if row:
            self.var_sup_invoice.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.txt_desc.delete('1.0', tk.END)
            self.txt_desc.insert(tk.END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Number must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice Number", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?",
                                (self.var_name.get(), self.var_contact.get(),
                                 self.txt_desc.get('1.0', tk.END).strip(), self.var_sup_invoice.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Number must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice Number", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier deleted successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', tk.END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice Number required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert("", tk.END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = tk.Tk()
    obj = supplierClass(root)
    root.mainloop()