import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess

class UserManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login and Register")

        # Increase font size
        font = ('Arial', 20)

        self.username_label = tk.Label(master, text="Username:", font=font)
        self.username_entry = tk.Entry(master, font=font)

        self.password_label = tk.Label(master, text="Password:", font=font)
        self.password_entry = tk.Entry(master, show="*", font=font)

        self.phone_label = tk.Label(master, text="Phone Number:", font=font)
        self.phone_entry = tk.Entry(master, font=font)

        self.login_button = tk.Button(master, text="Login", command=self.login, font=font)
        self.register_button = tk.Button(master, text="Register", command=self.register, font=font)

        # Increase padding
        padx_value = 20
        pady_value = 20

        # Grid layout with increased padding
        self.username_label.grid(row=0, column=0, sticky="E", pady=pady_value, padx=padx_value)
        self.username_entry.grid(row=0, column=1, pady=pady_value, padx=padx_value)
        self.password_label.grid(row=1, column=0, sticky="E", pady=pady_value, padx=padx_value)
        self.password_entry.grid(row=1, column=1, pady=pady_value, padx=padx_value)
        self.phone_label.grid(row=2, column=0, sticky="E", pady=pady_value, padx=padx_value)
        self.phone_entry.grid(row=2, column=1, pady=pady_value, padx=padx_value)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=pady_value, padx=padx_value)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=pady_value, padx=padx_value)

        # Ensure user_data.json file exists
        self.ensure_user_data_file()

    def ensure_user_data_file(self):
        if not os.path.exists("user_data.json"):
            with open("user_data.json", "w") as file:
                json.dump({}, file)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open("user_data.json", "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                messagebox.showerror("Login Error", "Invalid JSON syntax in user data file.")
                return

        if username in users and users[username]['password'] == password:
            root.destroy()
            messagebox.showinfo("Login", "Login successful!")
            subprocess.run(["python3", "mainui.py"])
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()

        if not username or not password or not phone:
            messagebox.showerror("Registration Error", "Username, password, and phone number are required.")
            return

        with open("user_data.json", "r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                messagebox.showerror("Registration Error", "Invalid JSON syntax in user data file.")
                return

        if username in users:
            messagebox.showerror("Registration Error", "Username already exists.")
        else:
            users[username] = {'password': password, 'phone': phone}
            with open("user_data.json", "w") as file:
                json.dump(users, file)
            root.destroy()
            messagebox.showinfo("Registration", "Registration successful!")
            subprocess.run(["python3", "mainui.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)

    # Enable secure coding
    root.attributes('-topmost', 1)
    root.attributes('-topmost', 0)

    root.mainloop()
