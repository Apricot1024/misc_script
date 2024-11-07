from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

def calculate_time_difference():
    try:
        time1 = datetime.strptime(entry_time1.get(), '%Y/%m/%d/%H/%M/%S')
        time2 = datetime.strptime(entry_time2.get(), '%Y/%m/%d/%H/%M/%S')
        difference = abs(time2 - time1)
        messagebox.showinfo("Time Difference", f"Time Difference: {difference}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date and time in YYYY/MM/DD/HH/mm/ss format")

def calculate_new_time():
    try:
        time = datetime.strptime(entry_time.get(), '%Y/%m/%d/%H/%M/%S')
        seconds = int(entry_seconds.get())
        new_time = time + timedelta(seconds=seconds)
        messagebox.showinfo("New Time", f"New Time: {new_time.strftime('%Y/%m/%d/%H/%M/%S')}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid date and time in YYYY/MM/DD/HH/mm/ss format and seconds as integer")

def convert_seconds():
    try:
        seconds = int(entry_convert_seconds.get())
        days = seconds // (24 * 3600)
        seconds %= (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        messagebox.showinfo("Converted Time", f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter seconds as integer")

root = tk.Tk()
root.title("Time Calculator")

tk.Label(root, text="Time 1 (YYYY/MM/DD/HH/mm/ss):").grid(row=0, column=0)
entry_time1 = tk.Entry(root)
entry_time1.grid(row=0, column=1)

tk.Label(root, text="Time 2 (YYYY/MM/DD/HH/mm/ss):").grid(row=1, column=0)
entry_time2 = tk.Entry(root)
entry_time2.grid(row=1, column=1)

tk.Button(root, text="Calculate Difference", command=calculate_time_difference).grid(row=2, column=0, columnspan=2)

tk.Label(root, text="Time (YYYY/MM/DD/HH/mm/ss):").grid(row=3, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=3, column=1)

tk.Label(root, text="Seconds to Add/Subtract:").grid(row=4, column=0)
entry_seconds = tk.Entry(root)
entry_seconds.grid(row=4, column=1)

tk.Button(root, text="Calculate New Time", command=calculate_new_time).grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Seconds to Convert:").grid(row=6, column=0)
entry_convert_seconds = tk.Entry(root)
entry_convert_seconds.grid(row=6, column=1)

tk.Button(root, text="Convert Seconds", command=convert_seconds).grid(row=7, column=0, columnspan=2)

root.mainloop()