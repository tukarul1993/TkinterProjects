import tkinter as tk
import pyodbc

# create a window with a specific size
window = tk.Tk()
window.geometry("400x300")

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

# create a frame to hold the grid and add a scroll bar
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# create a frame to hold the data in the grid
grid = tk.Frame(canvas)
canvas.create_window((0, 0), window=grid, anchor='nw')

# function to edit data
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

    # clear any existing labels in the grid
    for child in grid.winfo_children():
        child.destroy()

    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            label = tk.Label(grid, text=value)
            label.grid(row=i, column=j)
        # add an "Edit" button at the end of the row
        edit_button = tk.Button(grid, text="Edit", command=lambda row=row: edit_data(row))
        edit_button.grid(row=i, column=j + 1)
    conn.close()

load_data()

# run the window
window.mainloop()
