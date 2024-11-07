import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class TimeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Calculator")

        self.create_widgets()

    def create_widgets(self):
        self.start_label = ttk.Label(self.root, text="Start Time (YYYY/MM/DD/HH/mm/ss):")
        self.start_label.grid(column=0, row=0, padx=10, pady=5)
        self.start_entry = ttk.Entry(self.root)
        self.start_entry.grid(column=1, row=0, padx=10, pady=5)

        self.end_label = ttk.Label(self.root, text="End Time (YYYY/MM/DD/HH/mm/ss):")
        self.end_label.grid(column=0, row=1, padx=10, pady=5)
        self.end_entry = ttk.Entry(self.root)
        self.end_entry.grid(column=1, row=1, padx=10, pady=5)

        self.calc_diff_button = ttk.Button(self.root, text="Calculate Difference", command=self.calculate_difference)
        self.calc_diff_button.grid(column=0, row=2, padx=10, pady=5)

        self.diff_result_label = ttk.Label(self.root, text="")
        self.diff_result_label.grid(column=1, row=2, padx=10, pady=5)

        self.time_label = ttk.Label(self.root, text="Time (YYYY/MM/DD/HH/mm/ss):")
        self.time_label.grid(column=0, row=3, padx=10, pady=5)
        self.time_entry = ttk.Entry(self.root)
        self.time_entry.grid(column=1, row=3, padx=10, pady=5)

        self.delta_label = ttk.Label(self.root, text="Time Delta (days, seconds):")
        self.delta_label.grid(column=0, row=4, padx=10, pady=5)
        self.delta_entry = ttk.Entry(self.root)
        self.delta_entry.grid(column=1, row=4, padx=10, pady=5)

        self.calc_new_time_button = ttk.Button(self.root, text="Calculate New Time", command=self.calculate_new_time)
        self.calc_new_time_button.grid(column=0, row=5, padx=10, pady=5)

        self.new_time_result_label = ttk.Label(self.root, text="")
        self.new_time_result_label.grid(column=1, row=5, padx=10, pady=5)

    def calculate_difference(self):
        start_time = datetime.strptime(self.start_entry.get(), "%Y/%m/%d/%H/%M/%S")
        end_time = datetime.strptime(self.end_entry.get(), "%Y/%m/%d/%H/%M/%S")
        diff = end_time - start_time
        self.diff_result_label.config(text=str(diff))

    def calculate_new_time(self):
        time = datetime.strptime(self.time_entry.get(), "%Y/%m/%d/%H/%M/%S")
        delta_days, delta_seconds = map(int, self.delta_entry.get().split(","))
        new_time = time + timedelta(days=delta_days, seconds=delta_seconds)
        self.new_time_result_label.config(text=new_time.strftime("%Y/%m/%d/%H/%M/%S"))

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeCalculator(root)
    root.mainloop()