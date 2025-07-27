from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import subprocess

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login System | Developed by: Apoorv Misra")
        self.root.config(bg="#fafafa")

        # ===images===#
        self.phone_image = ImageTk.PhotoImage(file="C:\\Mini Project\\images\\phone.png")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image,bd=0).place(x=200, y=50)

        #===Login Frame===#
        self.employee_id = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)
        title = Label(login_frame, text="Login System", font=("Elephant", 30,"bold"), bg="white").place(x=0, y=30, relwidth=1)

        lbl_user=Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=100)
        txt_employee_id = Entry(login_frame,textvariable=self.employee_id, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=140, width=250, height=35)
        
        lbl_pass=Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=200)
        txt_pass = Entry(login_frame,textvariable=self.password,show="*", font=("times new roman", 15), bg="#ECECEC").place(x=50, y=240, width=250, height=35)

        btn_login = Button(login_frame,command=self.login, text="Login", font=("Arial RounDED MT Bold", 20), bg="#00B0f0",activebackground="#00B0F0", fg="white",activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)
        
        hr=Label(login_frame, bg="lightgray").place(x=50, y=370,width=250, height=2)
        or_=Label(login_frame, text="OR", font=("times new roman", 15,"bold"), bg="white",fg="lightgray").place(x=150, y=355)
        btn_forget = Button(login_frame,command=self.forget_window, text="Forgot Password?", font=("times new roman", 15), bg="white", fg="#00759E", bd=0, cursor="hand2").place(x=100, y=400)

       ##===Frame2===#
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        lbl_reg=Label(register_frame, text="Developed By Apoorv (EN22CS301188)\n & Arpita (EN22CS301201)", font=("times new roman", 15), bg="white").place(x=0, y=5, relwidth=1)
        #btn_signup=Button(register_frame, text="Sign Up", font=("times new roman", 15,"bold"), bg="white", fg="#00759E", bd=0, cursor="hand2").place(x=225, y=9)

        #===Animation Images===#
        self.im1 = ImageTk.PhotoImage(file="C:\\Mini Project\\images\\im1.png")
        self.im2 = ImageTk.PhotoImage(file="C:\\Mini Project\\images\\im2.png")
        self.im3 = ImageTk.PhotoImage(file="C:\\Mini Project\\images\\im3.png")
        
        self.lbl_change_image = Label(self.root, bd=0, bg="gray")
        self.lbl_change_image.place(x=367, y=153, width=240, height=428)
        self.animate()

#=================================ALL FUNCTIONS=================================#

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(1000, self.animate)


    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                # Fetch the user from the database
                cur.execute("SELECT utype FROM employee WHERE eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()  # Correctly assign the result to 'user'
                
                if user is None:  # Check if no user is found
                    messagebox.showerror("Error", "Invalid Employee ID or Password", parent=self.root)
                else:
                    user_type = user[0]  # Extract the user type from the tuple
                    if user_type == "Admin":
                        self.root.destroy()
                        subprocess.Popen(["python", "C:\\Mini Project\\employee.py"])
                    else:
                        self.root.destroy()
                        subprocess.Popen(["python", "C:\\Mini Project\\dashboard.py"])

                    # Successful login
                    messagebox.showinfo("Success", f"Welcome {self.employee_id.get()}!", parent=self.root)  # Display a welcome message
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


    def forget_window(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:  
            if self.employee_id.get() == "":
                messagebox.showerror("Error", "Please enter your Employee ID to reset password", parent=self.root)
            else:
                cur.execute("SELECT email FROM employee WHERE eid=?", (self.employee_id.get(),))
                result = cur.fetchone()  # Fetch the email from the database
                
                if result is None:  # Check if no email is found
                    messagebox.showerror("Error", "Employee ID not found, try again", parent=self.root)
                else:
                    email = result[0]  # Extract the email from the tuple
                    
                    # ====== Forget Window ====== #
                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_confirm_pass = StringVar()
                    
                    # Create the reset password window
                    self.forgot_window = Toplevel(self.root)
                    self.forgot_window.title("Reset Password")
                    self.forgot_window.geometry("400x350+500+100")
                    self.forgot_window.focus_force()

                    title = Label(self.forgot_window, text="Reset Password", font=("times new roman", 20, "bold"), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                    lbl_reset = Label(self.forgot_window, text="Enter OTP sent on registered Email", font=("times new roman", 15), bg="white").place(x=20, y=70)
                    txt_reset = Entry(self.forgot_window, textvariable=self.var_otp, font=("times new roman", 15), bg="lightyellow").place(x=20, y=100, width=250, height=35)
                    self.btn_reset = Button(self.forgot_window, text="Verify OTP", command=self.verify_otp, font=("times new roman", 15), bg="lightblue")
                    self.btn_reset.place(x=280, y=100, width=100, height=35)

                    lbl_new_pass = Label(self.forgot_window, text="New Password", font=("times new roman", 15), bg="white").place(x=20, y=150)
                    txt_new_pass = Entry(self.forgot_window, textvariable=self.var_new_pass, show="*", font=("times new roman", 15), bg="lightyellow").place(x=20, y=180, width=250, height=35)
                    lbl_confirm_pass = Label(self.forgot_window, text="Confirm Password", font=("times new roman", 15), bg="white").place(x=20, y=220)
                    txt_confirm_pass = Entry(self.forgot_window, textvariable=self.var_confirm_pass, show="*", font=("times new roman", 15), bg="lightyellow").place(x=20, y=250, width=250, height=35)

                    self.btn_update = Button(self.forgot_window, text="Update", state=DISABLED, command=self.update_password, font=("times new roman", 15), bg="lightblue")
                    self.btn_update.place(x=150, y=300, width=100, height=35)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


    def verify_otp(self):
        # Example OTP verification logic
        entered_otp = self.var_otp.get()
        correct_otp = "123456"  # Replace this with the actual OTP logic (e.g., send OTP via email)
        if entered_otp == "":
            messagebox.showerror("Error", "Please enter the OTP", parent=self.forgot_window)
        elif entered_otp == correct_otp:
            messagebox.showinfo("Success", "OTP Verified! You can now reset your password.", parent=self.forgot_window)
            self.btn_update.config(state=NORMAL)  # Enable the Update button
        else:
            messagebox.showerror("Error", "Invalid OTP, please try again", parent=self.forgot_window)


    def update_password(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_new_pass.get() == "" or self.var_confirm_pass.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.forgot_window)
            elif self.var_new_pass.get() != self.var_confirm_pass.get():
                messagebox.showerror("Error", "New Password and Confirm Password must match", parent=self.forgot_window)
            else:
                # Update the password in the database
                cur.execute("UPDATE employee SET pass=? WHERE eid=?", (self.var_new_pass.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success", "Password updated successfully", parent=self.forgot_window)
                self.forgot_window.destroy()  # Close the reset password window
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.forgot_window)
        finally:
            con.close()
            

root = Tk()
obj = Login_System(root)
root.mainloop()
