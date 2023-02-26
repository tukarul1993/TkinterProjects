import tkinter as tk
import pyodbc

# create a window with a specific size
window = tk.Tk()
window.geometry("300x300")

# create labels and entry fields for the data to be entered
label1 = tk.Label(window, text="Name")
label1.pack()
entry1 = tk.Entry(window, width=20)
entry1.pack()

label2 = tk.Label(window, text="Age")
label2.pack()
entry2 = tk.Entry(window, width=20)
entry2.pack()


# create a button to save the data to the SQL Server database
def save_data():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=192.168.0.109,1433;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pyDE_Students (Name, Age) VALUES (?, ?)",
                   (entry1.get(), entry2.get()))
    conn.commit()
    conn.close()
    load_data()


save_button = tk.Button(window, text="Save", command=save_data)
save_button.pack()

# create a grid to display the saved data
grid = tk.Frame(window)
grid.pack()

def edit_data(row):
    print(row)

# function to load the data from the SQL Server database and display it on the grid
def load_data():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=192.168.0.109,1433;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Name, Age FROM pyDE_Students order by Id")
    rows = cursor.fetchall()



    for i, row in enumerate(rows):
        print(i,row)
        for j, value in enumerate(row):
            label = tk.Label(grid, text=value)
            label.grid(row=i, column=j)
            print(value)
        # add an "Edit" button at the end of the row
        edit_button = tk.Button(grid, text="Edit", command=edit_data(row))
        edit_button.grid(row=i, column=j + 1)
    conn.close()


load_data()

# run the window
window.mainloop()

"""
# function to save the edited data back to the SQL Server database
def save_edited_data():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=192.168.0.109;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()
    for i, row in enumerate(grid.winfo_children()):
        if i % 3 == 0:
            id = row.cget("text")
            print("id:",id)
            continue
        elif i % 3 == 1:
            name_widget = row
        else:
            age_widget = row
            if isinstance(name_widget, tk.Entry) and isinstance(age_widget, tk.Entry):
                name = name_widget.get()
                age = age_widget.get()
                cursor.execute("UPDATE pyDE_Students SET Name = ?, Age = ? WHERE Name = ?",
                               (name, age, name))
    conn.commit()
    conn.close()
"""

# create a button to save the edited data back to the SQL Server database
#save_edited_button = tk.Button(window, text="Save Edited Data", command=save_edited_data)
#save_edited_button.pack()

# run the window
#window.mainloop()
