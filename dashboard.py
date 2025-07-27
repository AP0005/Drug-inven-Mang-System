import tkinter as tk
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass 
from product import productClass
from sales import salesClass
import subprocess

class IMS:
    def __init__(self, root):  # Corrected from _init_ to __init__
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by: Apoorv Misra")
        self.root.config(bg="white")

        # Title label
        try:
            self.icon_title = tk.PhotoImage(file="C:\\Mini Project\\images\\logo1.png")
            title = tk.Label(self.root, text="Inventory Management System", image=self.icon_title, compound="left", font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
            title.place(x=0, y=0, relwidth=1, height=70)
        except tk.TclError:
            print("Error: Unable to load the image. Please check the file path and format.")


        # button logout
        btn_logout = tk.Button(self.root, text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg="red",cursor="hand2").place(x=1130, y=20, width=150, height=30)
       
        #--clock--
        self.lbl_clock= tk.Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)


        # Left Menu
        self.Menulogo= Image.open("C:\Mini Project\images\menu_im.png")
        self.Menulogo = self.Menulogo.resize((200,200))
        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)
        LeftMenu = tk.Frame(self.root, bd=2, relief=tk.RIDGE,bg="white")
        LeftMenu.place(x=5, y=102, width=200, height=780)

        lbl_menuLogo = tk.Label(LeftMenu, image=self.Menulogo)
        lbl_menuLogo.pack(side=tk.TOP, fill=tk.X)

        self.icon_side=tk.PhotoImage(file="C:\Mini Project\images\side.png")
        lbl_menu=tk.Label(LeftMenu,text="Menu",font=("times new roman", 20), bg="#009688").pack(side=tk.TOP, fill=tk.X)
        btn_employee=tk.Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)
        btn_supplier=tk.Button(LeftMenu,text="Suppliers",command =self.supplier,image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)
        btn_category=tk.Button(LeftMenu,text="Category", command=self.category,image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)
        btn_product=tk.Button(LeftMenu,text="Products",command=self.product,image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)
        btn_sales=tk.Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)
        btn_exit=tk.Button(LeftMenu,text="Exit",image=self.icon_side, compound="left",padx=20,anchor="w",font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=tk.TOP, fill=tk.X)


        #--Content--

        self.lbl_employee= tk.Label(self.root, text="Total Employees\n[ 0 ]",font=("goudy old style", 20, "bold"),bd=5,relief="ridge", bg="#33bbf9", fg="white")
        self.lbl_employee.place(x=250, y=120, width=250, height=150)

        self.lbl_supplier= tk.Label(self.root, text="Total Supplier\n[ 0 ]",font=("goudy old style", 20, "bold"),bd=5,relief="ridge", bg="#ff5722", fg="white")
        self.lbl_supplier.place(x=650, y=120, width=250, height=150)

        self.lbl_category= tk.Label(self.root, text="Total Category\n[ 0 ]",font=("goudy old style", 20, "bold"),bd=5,relief="ridge", bg="#009688", fg="white")
        self.lbl_category.place(x=1000, y=120, width=250, height=150)

        self.lbl_product= tk.Label(self.root, text="Total Products\n[ 0 ]",font=("goudy old style", 20, "bold"),bd=5,relief="ridge", bg="#607d8b", fg="white")
        self.lbl_product.place(x=250, y=300, width=250, height=150)

        self.lbl_sales= tk.Label(self.root, text="Total Sales\n[ 0 ]",font=("goudy old style", 20, "bold"),bd=5,relief="ridge", bg="#ffc107", fg="white")
        self.lbl_sales.place(x=650, y=300, width=250, height=150)



        #--footer--
        lbl_footer= tk.Label(self.root, text="IMS-Inventory Management System | Developed by: Apoorv Misra\nFor any Technical Issues Contact: 890xxxxx1",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=tk.BOTTOM, fill=tk.X)

    def employee(self):
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):  # Fixed indentation
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):  # Fixed indentation
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):  # Fixed indentation
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sales(self):  # Fixed indentation           
        self.new_win = tk.Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def logout(self):
        self.root.destroy()
        subprocess.call(["python", "login.py"])

# Create the Tkinter root window and run the application
if __name__ == "__main__":  # Corrected from _name_ to __name__
    root = tk.Tk()
    obj = IMS(root)
    root.mainloop()