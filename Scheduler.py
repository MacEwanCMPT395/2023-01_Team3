import tkinter as tk
import ttkbootstrap as ttk           #pip install ttkboostrap
from ttkbootstrap.constants import *
from tkinter import filedialog
from ttkbootstrap.tableview import Tableview
import pandas as pd                  #pip install pandas


class SchedulerApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Scheduler App")
        self.window.geometry("750x450")

        self.classroom_capacity = None

        self.import_btn = ttk.Button(
            text="Import Classroom CSV", 
            command=lambda: [self.import_csv(), self.create_table()], 
            width=20
        )
        self.import_btn.pack(side=TOP, padx=100, pady=20)

    # Import csv for classroom capacity info
    def import_csv(self):
        filepath = filedialog.askopenfilename()
        self.classroom_capacity = pd.read_csv(filepath)
        print(self.classroom_capacity)

    def create_table(self):
        tv = ttk.tableview.Tableview(
            master = self.window,
            paginated=True,
            searchable=False,
            bootstyle=PRIMARY,
            pagesize=10,
            height=10,
        )
        l1 = list(self.classroom_capacity)
        r_set = self.classroom_capacity.to_numpy().tolist()
        tv.build_table_data(l1, r_set)
        tv.load_table_data()
        tv.autoalign_columns()

        tv.pack(padx=5, pady=5) # Tableview is placed

# App Window Structure
window = ttk.Window(themename="superhero") #https://ttkbootstrap.readthedocs.io/en/latest/
app = SchedulerApp(window)
window.mainloop()
