from tkinter import Tk, IntVar, Radiobutton, Label, Entry, Button, messagebox
import tkinter as tk
import os

def show_age_specific_questions(age):
    if 10 <= age < 20:
        root.destroy()
        os.system("/usr/local/bin/python3 /Users/dd/Downloads/MentalHealthSIH20noon/App_1.py")
        
    elif 20 <= age < 40:
        root.destroy()
        os.system("/usr/local/bin/python3 /Users/dd/Downloads/MentalHealthSIH20noon/App_2.py")
        
    elif 40 <= age < 60:
        root.destroy()
        os.system("/usr/local/bin/python3 /Users/dd/Downloads/MentalHealthSIH20noon/App_3.py")
        

def show_common_questions():
    root.destroy()
    os.system("/usr/local/bin/python3 /Users/dd/Downloads/MentalHealthSIH20noon/App.py")
    

def process_input():
    if var.get() == 1:  # If "Yes" is selected
        try:
            age = int(entry.get())
            if 0 <= age <= 120:  # Assuming a reasonable age range
                show_age_specific_questions(age)
            else:
                messagebox.showwarning('Invalid Age', 'Please enter a valid age.')
        except ValueError:
            messagebox.showwarning('Invalid Input', 'Please enter a valid numerical age.')
    else:  # If "No" is selected
        show_common_questions()

    

# Create main root
root = Tk()
root.title('Chatbot UI')

root.geometry('500x400')

# Create widgets
label = Label(root, text='Do you want age-specific conversation?:', font=('Arial', 25))
label.pack(pady=20)

var = IntVar()
radio_button_yes = Radiobutton(root, text='Yes', variable=var, value=1, font=('Arial', 20), width=15)
radio_button_no = Radiobutton(root, text='No', variable=var, value=0, font=('Arial', 20), width=15)
radio_button_yes.pack()
radio_button_no.pack()

entry_label = Label(root, text='Enter Age:', font=('Arial', 14))
entry_label.pack(pady=10)

entry = Entry(root, font=('Arial', 20), width=10)
entry.pack(pady=10)

submit_button = Button(root, text='Submit', command=process_input, font=('Arial', 14))
submit_button.pack()

# Hide age input initially
entry_label.pack_forget()
entry.pack_forget()

# Function to toggle age input visibility
def toggle_age_input(*args):
    if var.get() == 1:
        entry_label.pack(pady=10)
        entry.pack(pady=10)
    else:
        entry_label.pack_forget()
        entry.pack_forget()

# Bind the toggle function to the radio button
var.trace_add("write", toggle_age_input)

# Run the application
root.mainloop()