import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class TimeCalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Calculator")
        self.geometry("400x400")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.create_time_diff_tab()
        self.create_time_add_subtract_tab()
        self.create_time_convert_tab()

    def create_time_diff_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Time Difference')

        # First Time Entry
        ttk.Label(frame, text='Start Time (YYYY/MM/DD/HH/mm/ss):').pack()
        self.start_time_entry = ttk.Entry(frame)
        self.start_time_entry.pack()

        # Second Time Entry
        ttk.Label(frame, text='End Time (YYYY/MM/DD/HH/mm/ss):').pack()
        self.end_time_entry = ttk.Entry(frame)
        self.end_time_entry.pack()

        # Calculate Button
        calc_button = ttk.Button(frame, text='Calculate Difference', command=self.calculate_difference)
        calc_button.pack()

        # Result Label
        self.diff_result_label = ttk.Label(frame, text='')
        self.diff_result_label.pack()

    def create_time_add_subtract_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Add/Subtract Time')

        # Base Time Entry
        ttk.Label(frame, text='Base Time (YYYY/MM/DD/HH/mm/ss):').pack()
        self.base_time_entry = ttk.Entry(frame)
        self.base_time_entry.pack()

        # Time Period Entry
        ttk.Label(frame, text='Time Period (HH:mm:ss):').pack()
        self.time_period_entry = ttk.Entry(frame)
        self.time_period_entry.pack()

        # Add/Subtract Option
        self.operation = tk.StringVar(value='Add')
        ttk.Radiobutton(frame, text='Add', variable=self.operation, value='Add').pack()
        ttk.Radiobutton(frame, text='Subtract', variable=self.operation, value='Subtract').pack()

        # Calculate Button
        calc_button = ttk.Button(frame, text='Calculate New Time', command=self.calculate_new_time)
        calc_button.pack()

        # Result Label
        self.new_time_result_label = ttk.Label(frame, text='')
        self.new_time_result_label.pack()

    def create_time_convert_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text='Convert Time')

        # Time Period Entry
        ttk.Label(frame, text='Time Period (HH:mm:ss or seconds):').pack()
        self.convert_time_entry = ttk.Entry(frame)
        self.convert_time_entry.pack()

        # Conversion Options
        self.convert_option = tk.StringVar(value='To Seconds')
        ttk.Radiobutton(frame, text='HH:mm:ss → Seconds', variable=self.convert_option, value='To Seconds').pack()
        ttk.Radiobutton(frame, text='Seconds → HH:mm:ss', variable=self.convert_option, value='To HH:mm:ss').pack()

        # Convert Button
        convert_button = ttk.Button(frame, text='Convert', command=self.convert_time)
        convert_button.pack()

        # Result Label
        self.convert_result_label = ttk.Label(frame, text='')
        self.convert_result_label.pack()

    def calculate_difference(self):
        try:
            fmt = '%Y/%m/%d/%H/%M/%S'
            start_time_str = self.start_time_entry.get()
            end_time_str = self.end_time_entry.get()
            start_time = datetime.strptime(start_time_str, fmt)
            end_time = datetime.strptime(end_time_str, fmt)
            diff = end_time - start_time
            self.diff_result_label.config(text=f'Difference: {diff}')
        except ValueError:
            self.diff_result_label.config(text='Invalid time format.')

    def calculate_new_time(self):
        try:
            fmt = '%Y/%m/%d/%H/%M/%S'
            base_time_str = self.base_time_entry.get()
            base_time = datetime.strptime(base_time_str, fmt)
            period_str = self.time_period_entry.get()
            h, m, s = map(int, period_str.split(':'))
            delta = timedelta(hours=h, minutes=m, seconds=s)
            if self.operation.get() == 'Add':
                new_time = base_time + delta
            else:
                new_time = base_time - delta
            self.new_time_result_label.config(text=f'New Time: {new_time.strftime(fmt)}')
        except ValueError:
            self.new_time_result_label.config(text='Invalid time format.')

    def convert_time(self):
        try:
            input_str = self.convert_time_entry.get()
            if self.convert_option.get() == 'To Seconds':
                h, m, s = map(int, input_str.split(':'))
                total_seconds = h * 3600 + m * 60 + s
                self.convert_result_label.config(text=f'Total Seconds: {total_seconds}')
            else:
                total_seconds = int(input_str)
                h = total_seconds // 3600
                m = (total_seconds % 3600) // 60
                s = total_seconds % 60
                self.convert_result_label.config(text=f'Time Period: {h:02d}:{m:02d}:{s:02d}')
        except ValueError:
            self.convert_result_label.config(text='Invalid input.')

if __name__ == '__main__':
    app = TimeCalcApp()
    app.mainloop()