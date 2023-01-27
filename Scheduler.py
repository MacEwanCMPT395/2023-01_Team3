import tkinter as tk
import ttkbootstrap as ttk           #pip install ttkboostrap
from ttkbootstrap.constants import *
from tkinter import filedialog
from ttkbootstrap.tableview import Tableview
import pandas as pd                  #pip install pandas


# App Window Structure
window = ttk.Window(themename="superhero")   #https://ttkbootstrap.readthedocs.io/en/latest/
window.title("Scheduler App")
window.geometry("750x450")

# Import csv for classroom capacity info
def import_csv():
    global classroom_capacity
    filepath = filedialog.askopenfilename()
    classroom_capacity = pd.read_csv(filepath)
    print(classroom_capacity)

def create_table():
    tv = ttk.tableview.Tableview(
    master = window,
    paginated=True,
    searchable=False,
    bootstyle=PRIMARY,
    pagesize=10,
    height=10,)
    l1= list(classroom_capacity)
    r_set = classroom_capacity.to_numpy().tolist()
    tv.build_table_data(l1,r_set) # built in functions for Tableview 
    tv.load_table_data()
    tv.autoalign_columns()
    
    tv.pack(padx=5, pady=5)  # Tableview is placed

# App features
import_btn = ttk.Button(
            text="Import Classroom CSV", 
            command=lambda: [import_csv(), create_table()], 
            width=20
        )
import_btn.pack(side=TOP, padx=100, pady=20)


window.mainloop()
