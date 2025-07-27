import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):  # Corrected from _init_ to __init__
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by: Apoorv Misra")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===all variable===
        self.var_searchby = tk.StringVar()
        self.var_searchtxt = tk.StringVar()

        self.var_emp_id = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_contact = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_doj = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_pass = tk.StringVar()
        self.var_utype = tk.StringVar()
        self.var_salary = tk.StringVar()

        # ===search frame===
        SearchFrame = tk.LabelFrame(self.root, text="Search employee", font=("goudy old style", 12, "bold"), bd=2, relief="ridge", bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ===options===
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Employee ID", "Name", "Contact"), state="readonly", justify="center", font=("goudy old style", 15))
        cmb_search.place(x=12, y=10, width=180)
        cmb_search.current(0)

        txt_search = tk.Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10, width=200)
        btn_search = tk.Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15, "bold"), bg="#4caf50", highlightbackground="#4caf50", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        # ===title===
        title = tk.Label(self.root, text="Employee Details", font=("goudy old style", 20), bg="#1167b1", fg="white").place(x=50, y=100, width=1000)

        # ===content===

        # ==row1===
        lbl_empid = tk.Label(self.root, text="Emp ID", font=("goudy old style", 20), bg="white").place(x=50, y=150)
        lbl_gender = tk.Label(self.root, text="Gender", font=("goudy old style", 20), bg="white").place(x=350, y=150)
        lbl_contact = tk.Label(self.root, text="Contact", font=("goudy old style", 20), bg="white").place(x=750, y=150)

        lbl_empid = tk.Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 20), bg="lightyellow")
        lbl_empid.place(x=150, y=150, width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Others"), state="readonly", justify="center", font=("goudy old style", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)

        lbl_contact = tk.Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 20), bg="lightyellow")
        lbl_contact.place(x=850, y=150, width=180)

        # ==row2===
        lbl_name = tk.Label(self.root, text="Name", font=("goudy old style", 20), bg="white").place(x=50, y=190)
        lbl_dob = tk.Label(self.root, text="D.O.B", font=("goudy old style", 20), bg="white").place(x=350, y=190)
        lbl_doj = tk.Label(self.root, text="D.O.J", font=("goudy old style", 20), bg="white").place(x=750, y=190)

        lbl_name = tk.Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20), bg="lightyellow")
        lbl_name.place(x=150, y=190, width=180)

        lbl_dob = tk.Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 20), bg="lightyellow")
        lbl_dob.place(x=500, y=190, width=180)

        lbl_doj = tk.Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 20), bg="lightyellow")
        lbl_doj.place(x=850, y=190, width=180)

        # ==row3===
        lbl_email = tk.Label(self.root, text="Email", font=("goudy old style", 20), bg="white").place(x=50, y=230)
        lbl_pass = tk.Label(self.root, text="Password", font=("goudy old style", 20), bg="white").place(x=350, y=230)
        lbl_utype = tk.Label(self.root, text="Usertype", font=("goudy old style", 20), bg="white").place(x=750, y=230)

        lbl_email = tk.Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20), bg="lightyellow")
        lbl_email.place(x=150, y=230, width=180)

        lbl_pass = tk.Entry(self.root, textvariable=self.var_pass, font=("goudy old style", 20), bg="lightyellow")
        lbl_pass.place(x=500, y=230, width=180)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state="readonly", justify="center", font=("goudy old style", 15))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # ==row4===
        lbl_address = tk.Label(self.root, text="Address", font=("goudy old style", 20), bg="white").place(x=50, y=270)
        lbl_salary = tk.Label(self.root, text="Salary", font=("goudy old style", 20), bg="white").place(x=500, y=270)

        self.txt_address = tk.Text(self.root, font=("goudy old style", 20), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        lbl_salary = tk.Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 20), bg="lightyellow").place(x=600, y=270, width=180)

        # ===buttons===
        btn_add = tk.Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = tk.Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = tk.Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = tk.Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ===employee details===
        emp_frame = tk.Frame(self.root, bd=3, relief="ridge")
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = tk.Scrollbar(emp_frame, orient=tk.VERTICAL)
        scrollx = tk.Scrollbar(emp_frame, orient=tk.HORIZONTAL)

        self.employeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)

        self.employeeTable.heading("eid", text="Emp ID")
        self.employeeTable.heading("name", text="Name")
        self.employeeTable.heading("email", text="Email")
        self.employeeTable.heading("gender", text="Gender")
        self.employeeTable.heading("contact", text="Contact")
        self.employeeTable.heading("dob", text="D.O.B")
        self.employeeTable.heading("doj", text="D.O.J")
        self.employeeTable.heading("pass", text="Password")
        self.employeeTable.heading("utype", text="Usertype")
        self.employeeTable.heading("address", text="Address")
        self.employeeTable.heading("salary", text="Salary")

        self.employeeTable["show"] = "headings"

        self.employeeTable.column("eid", width=90)
        self.employeeTable.column("name", width=100)
        self.employeeTable.column("email", width=100)
        self.employeeTable.column("gender", width=100)
        self.employeeTable.column("contact", width=100)
        self.employeeTable.column("dob", width=100)
        self.employeeTable.column("doj", width=100)
        self.employeeTable.column("pass", width=100)
        self.employeeTable.column("utype", width=100)
        self.employeeTable.column("address", width=100)
        self.employeeTable.column("salary", width=100)

        self.employeeTable.pack(fill=tk.BOTH, expand=1)
        self.employeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

# ==========================================functions========================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try another", parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee (eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', tk.END).strip(),
                            self.var_salary.get(),
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert("", tk.END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.employeeTable.focus()
        content = self.employeeTable.item(f)
        row = content['values']
        if row:
            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txt_address.delete('1.0', tk.END)
            self.txt_address.insert(tk.END, row[9])
            self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute(
                        "Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0', tk.END).strip(),  # Corrected from self.text_address
                            self.var_salary.get(),
                            self.var_emp_id.get(),
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.root)
                        self.show()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("")
        self.txt_address.delete('1.0', tk.END)  # Corrected from self.text_address
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select search option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                # Map search options to database column names
                search_column_map = {
                    "Employee ID": "eid",
                    "Name": "name",
                    "Contact": "contact"
                }
                search_column = search_column_map.get(self.var_searchby.get(), None)

                if search_column is None:
                    messagebox.showerror("Error", "Invalid search option", parent=self.root)
                else:
                    # Execute the query with the mapped column name
                    query = f"SELECT * FROM employee WHERE {search_column} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        for row in rows:
                            self.employeeTable.insert("", tk.END, values=row)
                    else:
                        messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = tk.Tk()
    obj = employeeClass(root)
    root.mainloop()