import tkinter as tk
from tkinter import messagebox
import subprocess

class WelcomeWindow:
    def __init__(self, master):
        self.master = master
        master.title("Welcome to Your App")

        # Configure window size and position
        window_width = 800
        window_height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Set background color
        master.configure(bg="#e0862b")  # Change background color to #ffb338

        # Greeting label
        self.label = tk.Label(
            master, text="Welcome to APNA App!", font=("Arial", 40, "bold"), fg="#2c3e50", bg="#e0862b"
        )  # Use your preferred font and font color
        self.label.pack(pady=80)

        # Button to enter another Python script
        self.enter_button = tk.Button(
            master,
            text="Let's Chat", # Change button text to "Let's Chat"
            command=self.enter_script,
            font=("Arial", 24, "bold"),
            fg="#059e1e",
            bg="#e74c3c",  # Use your preferred button color
            padx=20,
            pady=10,
            borderwidth=3,
            relief=tk.GROOVE,
            cursor="hand2",
            highlightbackground="#059e1e",  # Set the edge color to #32eb2f
            highlightcolor="#32eb2f",
        )
        self.rounded_button(self.enter_button, 20)  # Set button corner radius
        self.enter_button.pack(pady=50)

    def enter_script(self):
        # Code to execute when the button is clicked
        try:
            subprocess.run(["python3", "home.py"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def rounded_button(self, widget, radius):
        # Create a rounded button
        widget.bind("<Enter>", lambda e: self.on_enter(widget, radius))
        widget.bind("<Leave>", lambda e: self.on_leave(widget, radius))

    def on_enter(self, widget, radius):
        widget.config(bg="#c0392b")  # Change color on hover
        widget.config(relief=tk.FLAT)
        widget.config(borderwidth=3)

    def on_leave(self, widget, radius):
        widget.config(bg="#e74c3c")  # Change back to the original color
        widget.config(relief=tk.GROOVE)
        widget.config(borderwidth=3)

if __name__ == "__main__":
    root = tk.Tk()
    welcome_window = WelcomeWindow(root)
    root.mainloop()
