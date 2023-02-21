import tkinter as tk
import pyodbc

# create a window with a specific size
window = tk.Tk()
window.geometry("300x300")

# create labels and entry fields for the data to be entered
label1 = tk.Label(window, text="Id")
label1.pack()
entry_id = tk.Entry(window, width=20)
entry_id.pack()
label1 = tk.Label(window, text="Name")
label1.pack()
entry1 = tk.Entry(window, width=20)
entry1.pack()

label2 = tk.Label(window, text="Age")
label2.pack()
entry2 = tk.Entry(window, width=20)
entry2.pack()
entry_id['state'] = tk.DISABLED

# create a button to save the data to the SQL Server database
def save_data():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pyDE_Students (Name, Age) VALUES (?, ?)",(entry1.get(), entry2.get()))
    conn.commit()
    conn.close()
    load_data()

def update_data():

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    print("update pyDE_Students set Name=?, Age=? where Id =?",(entry1.get(), entry2.get(),entry_id.get()))
    cursor.execute("update pyDE_Students set Name=?, Age=? where Name =?",
                   (entry1.get(), entry2.get(),entry_id.get()))
    conn.commit()
    conn.close()
    load_data()

save_button = tk.Button(window, text="Save", command=save_data)
save_button.pack()
update_button = tk.Button(window, text="Update",command=update_data)
update_button.pack()
update_button['state']=tk.DISABLED

# create a grid to display the saved data
grid = tk.Frame(window)
grid.pack()

def edit_data(row):
    entry_id['state'] = "normal"
    entry_id.insert(0,row[0])
    entry_id['state'] = tk.DISABLED
    entry1.insert(0, row[1])
    entry2.insert(0, row[2])
    save_button['state'] = tk.DISABLED
    update_button['state'] = "normal"


# function to load the data from the SQL Server database and display it on the grid
def load_data():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Age FROM pyDE_Students")
    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            label = tk.Label(grid, text=value)
            label.grid(row=i, column=j)
            #print(value)
        # add an "Edit" button at the end of the row
        edit_button = tk.Button(grid, text="Edit", command=lambda row=row: edit_data(row))
                                #command=lambda: save_edited_data(row[0], name_entry.get(), age_entry.get()))
        edit_button.grid(row=i, column=j + 1)
    conn.close()


load_data()

# run the window
window.mainloop()
