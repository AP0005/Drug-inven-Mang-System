import tkinter as tk
from tkinter import ttk, messagebox, RAISED  # Added RAISED
from PIL import Image, ImageTk
import sqlite3

class categoryClass:
    def __init__(self, root):  # Corrected from _init_ to __init__
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed by: APOORV MISRA and ARPITA JAISWAL")
        self.root.config(bg="white")
        self.root.focus_force()

        #===Variables===#
        self.var_cat_id = tk.StringVar()
        self.var_name = tk.StringVar()

        # ===TITLE===#
        lbl_title = tk.Label(self.root, text="Manage Product Category", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=tk.RIDGE)
        lbl_title.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        lbl_name = tk.Label(self.root, text="Enter Category Name", font=("goudy old style", 30), bg="white").place(x=50, y=100)
        txt_name = tk.Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow").place(x=50, y=170, width=300)

        btn_add = tk.Button(self.root, text="ADD",command=self.add, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
        btn_delete = tk.Button(self.root, text="DELETE", command=self.delete, font=("goudy old style", 15), bg="red", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=30)


        # ===Category details===#
        cat_frame=tk.Frame(self.root,bd=3,relief="ridge")
        cat_frame.place(x=700,y=100,width=380,height=100)

        scrolly= tk.Scrollbar(cat_frame,orient=tk.VERTICAL)
        scrollx= tk.Scrollbar(cat_frame,orient=tk.HORIZONTAL)   

        self.category_table = ttk.Treeview(cat_frame,columns=("cid", "name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.category_table.heading("cid", text="C-ID")
        self.category_table.heading("name", text="Name")
        self.category_table["show"] = "headings"
        self.category_table.column("cid", width=90)
        self.category_table.column("name", width=100)

        scrollx.pack(side=tk.BOTTOM,fill=tk.X)
        scrolly.pack(side=tk.RIGHT,fill=tk.Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        self.category_table.pack(fill=tk.BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #===Images===#
        self.im1=Image.open("C:\Mini Project\images\cat.jpg")
        self.im1=self.im1.resize((500,250),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=tk.Label(self.root,image=self.im1,bd=2,relief=RAISED).place(x=50,y=220,width=500,height=200)

        self.im2=Image.open("C:\Mini Project\images\category.jpg")
        self.im2=self.im2.resize((500,250),Image.Resampling.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=tk.Label(self.root,image=self.im2,bd=2,relief=RAISED).place(x=580,y=220)

        self.init_db()

        self.show()

#==========================================functions========================================================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category already exists, try a different name", parent=self.root)
                else:
                    cur.execute("INSERT INTO category (name) VALUES (?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()  # Refresh the table
                    self.var_name.set("")  # Clear the input field
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('', 'end', values=row)  # Insert C-ID and Name
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def get_data(self, ev):
        f = self.category_table.focus()
        content = self.category_table.item(f)
        row = content['values']
        if row:  # Ensure row is not empty
            self.var_cat_id.set(row[0])  # Set C-ID
            self.var_name.set(row[1])  # Set category name


    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select a category from the list", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid category, please try again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete this category?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category deleted successfully", parent=self.root)
                        self.show()  # Refresh the table
                        self.var_cat_id.set("")  # Clear the C-ID field
                        self.var_name.set("")  # Clear the category name field
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def init_db(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS category (cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Error initializing database: {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = tk.Tk()
    obj = categoryClass(root)
    root.mainloop()