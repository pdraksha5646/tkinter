import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_date = entry.get()
        birth_date = datetime.strptime(birth_date, "%d-%m-%Y") 
        today = datetime.today()
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        messagebox.showinfo("Age Calculator", f"Your Age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter date in DD-MM-YYYY format.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Labels and input
label = tk.Label(root, text="Enter Birth Date (DD-MM-YYYY):", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Calculate Age", command=calculate_age, font=("Arial", 12), bg="lightblue")
button.pack(pady=20)

root.mainloop()
