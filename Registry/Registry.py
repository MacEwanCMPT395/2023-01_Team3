import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkcalendar import Calendar, DateEntry

#DB
import sqlite3
import csv

conn = sqlite3.connect("reg_data.db")
c= conn. cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userdata(firstname TEXT, lastname TEXT, email TEXT, age TEXT, DOB TEXT, address TEXT, phonenumber TEXT)')

def add_data(firstname, lastname, email, age, DOB, address, phonenumber):
    c.execute('INSERT INTO userdata(firstname, lastname, email, age, DOB, address, phonenumber) VALUES (?,?,?,?,?,?,?)', (firstname, lastname, email, age, DOB, address, phonenumber))
    conn.commit()

def view_all_users():
    c.execute('SELECT * from userdata')
    data = c.fetchall()
    for row in data:
        tree.insert("", tk.END, values=row)

def get_single_user(firstname):
    c.execute('SELECT * FROM userdata WHERE firstname= "{}"'.format(firstname))
    data = c.fetchall()
    return data

# Functions
def clear_text():
    entry_fname.delete('0', END)
    entry_lname.delete('0', END)
    entry_email.delete('0', END)
    entry_age.delete('0', END)
    entry_address.delete('0', END)
    entry_phone.delete('0', END)

def add_details():
    firstname = str(entry_fname.get())
    lastname = str(entry_lname.get())
    email = str(entry_email.get())
    age = str(entry_age.get())
    date_of_birth = str(cal.get())
    phone_number = str(entry_phone.get())
    address = str(entry_address.get())
    add_data(firstname, lastname, email, age, date_of_birth, address, phone_number)
    result = '\nFirst Name: {}, \nLast Name: {}, \nE-Mail: {}, \nAge: {}, \nDate of Birth: {}, \nPhone Number: {}, \nAddress: {}'.format(firstname, lastname, email, age, date_of_birth, phone_number, address)
    tab1_display.insert(tk.END, result)
    messagebox.showinfo(title= "Registry App", message = "User Added to Database")

def clear_result():
    tab1_display.delete('1.0',END)

# Export functions
def export_csv():
    filename = str(entry_filename.get())
    myfilename = filename + '.csv'
    with open(myfilename, 'w') as f:
        writer = csv.writer(f)
        c.execute('SELECT * FROM userdata')
        data = c.fetchall()
        writer.writerow(['firstname', 'lastname', 'email', 'age', 'date_of_birth', 'address', 'phone_number'])
        writer.writerows(data)
        messagebox.showinfo(title = "Registry APP", message = '"Success!\nExported As {}'.format(myfilename))

def export_xls():
    filename = str(entry_filename.get())
    myfilename = filename + '.xls'
    with open(myfilename, 'w') as f:
        writer = csv.writer(f)
        c.execute('SELECT * FROM userdata')
        data = c.fetchall()
        writer.writerow(['firstname', 'lastname', 'email', 'age', 'date_of_birth', 'address', 'phone_number'])
        writer.writerows(data)
        messagebox.showinfo(title = "Registry APP", message = '"Success!\nExported As {}'.format(myfilename))


# Structure and Layout
window = Tk() 
window.title("Registry")
window.geometry("750x450")

style = ttk.Style(window)
style.configure("lefttab.TNotebook", tabposition='wn')

#Tab Layout
tab_control = ttk.Notebook(window, style= 'lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# Add Tabs to Notbook
tab_control.add(tab1, text=f'{"Home":^30s}')
tab_control.add(tab2, text=f'{"View":^30s}')
tab_control.add(tab3, text=f'{"Search":^30s}')
tab_control.add(tab4, text=f'{"Export":^30s}')
tab_control.add(tab5, text=f'{"About":^30s}')

tab_control.pack(expand=1, fill="both")

create_table()

label1 = Label(tab1, text="Registry Practice App", padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text="View", padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text="Search", padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text="Export", padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text="About", padx=5, pady=5)
label5.grid(column=0, row=0)

# Home Tab

l1 = Label(tab1, text= "First Name", padx=5, pady=5)
l1.grid(column=0, row=1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1, textvariable= fname_raw_entry, width=40)
entry_fname.grid(row=1, column=1)

l2 = Label(tab1, text= "Last Name", padx=5, pady=5)
l2.grid(column=0, row=2)
lname_raw_entry = StringVar()
entry_lname = Entry(tab1, textvariable= lname_raw_entry, width=40)
entry_lname.grid(row=2, column=1)

l3 = Label(tab1, text= "Email", padx=5, pady=5)
l3.grid(column=0, row=3)
email_raw_entry = StringVar()
entry_email = Entry(tab1, textvariable= email_raw_entry, width=40)
entry_email.grid(row=3, column=1)

l4 = Label(tab1, text= "Age", padx=5, pady=5)
l4.grid(column=0, row=4)
age_raw_entry = StringVar()
entry_age = Entry(tab1, textvariable= age_raw_entry, width=40)
entry_age.grid(row=4, column=1)

l5 = Label(tab1, text= "Date of Birth", padx=5, pady=5)
l5.grid(column=0, row=5)
dob_raw_entry = StringVar()
cal = DateEntry(tab1, textvariable= dob_raw_entry, width=30, background= "darkblue", foreground= 'white', borderwidth=2, year=2023 )
cal.grid(row=5, column=1, padx=10, pady=10)

l6 = Label(tab1, text= "Address", padx=5, pady=5)
l6.grid(column=0, row=6)
address_raw_entry = StringVar()
entry_address = Entry(tab1, textvariable= address_raw_entry, width=40)
entry_address.grid(row=6, column=1)

l7 = Label(tab1, text= "Phone", padx=5, pady=5)
l7.grid(column=0, row=7)
phone_raw_entry = StringVar()
entry_phone = Entry(tab1, textvariable= phone_raw_entry, width=40)
entry_phone.grid(row=7, column=1)

button1 = Button(tab1, text="Submit", width=12, bg="#03A9F4", fg='#fff', command=add_details)
button1. grid(row=8, column=1, padx=5, pady=5)

button2 = Button(tab1, text="Clear", width=12, bg="#03A9F4", fg='#fff', command=clear_text)
button2.grid(row=8, column=0, padx=5, pady=5)

# Display screen
tab1_display = ScrolledText(tab1, height=5)
tab1_display.grid(row=10, column=1, padx=5, pady=5, columnspan=3)

button3 = Button(tab1, text="Clear Result", width=12, bg="#03A9F4", fg='#fff', command=clear_result)
button3.grid(row=12, column=1, padx=5, pady=5)

# View

button_view = Button(tab2, text="View All", width=12, bg="#03A9F4", fg='#fff', command=view_all_users)
button_view.grid(row=1, column=0, padx=10, pady=10)
tree= ttk.Treeview(tab2, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7",), show='headings')
tree.heading("#1", text="First Name")
tree.heading("#2", text="Last Name")
tree.heading("#3", text="E-mail")
tree.heading("#4", text="Age")
tree.heading("#5", text="DOB")
tree.heading("#6", text="Address")
tree.heading("#7", text="Phone Number")
tree.grid(row=10, column=0, columnspan=3, padx=5,pady=5)


# Export DB

label_export1= Label(tab4, text='File Name', padx=5, pady=5)
label_export1.grid(column=0, row=2)
filename_entry = StringVar()
entry_filename = Entry(tab4, textvariable=filename_entry, width=30)
entry_filename.grid(row=2, column=1)

csv_button = Button(tab4, text="TO CSV", width=12, bg="#03A9F4", fg='#fff', command=export_csv)
csv_button.grid(row=3, column=1, padx=10, pady=10)

xls_button = Button(tab4, text="TO XLS", width=12, bg="#03A9F4", fg='#fff', command=export_xls)
xls_button.grid(row=3, column=2, padx=10, pady=10)




window.mainloop()