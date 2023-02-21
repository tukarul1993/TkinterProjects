import pyodbc
import tkinter as tk
from tkinter import ttk

# Connect to MSSQL database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')

# Define a function to execute SQL query and populate the grid
def populate_grid():
    # Execute SQL query to retrieve data
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test')
    data = cursor.fetchall()

    # Create the grid and populate it with the retrieved data
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            entry = ttk.Entry(frame, width=10)
            entry.grid(row=i+1, column=j)
            entry.insert(0, str(value))
            entry.bind('<FocusOut>', update_database)

# Define a function to update the database when the user edits the grid
def update_database(event):
    # Get the edited value and the row and column of the edited cell
    widget = event.widget
    row, col = int(widget.grid_info()['row']) - 1, int(widget.grid_info()['column'])
    value = widget.get()

    # Execute SQL query to update the corresponding row and column in the database
    cursor = conn.cursor()
    cursor.execute(f"UPDATE test SET Name='{value}' WHERE ID={row+1}")
    conn.commit()

# Create a tkinter window and a frame to hold the grid
root = tk.Tk()
root.title("MSSQL Grid")
frame = ttk.Frame(root)
frame.pack()

# Add headers to the grid
headers = ['ID', 'Column 1', 'Column 2', 'Column 3']
for i, header in enumerate(headers):
    label = ttk.Label(frame, text=header)
    label.grid(row=0, column=i)

# Call the populate_grid function to create the grid and populate it with data
populate_grid()

# Start the tkinter event loop
root.mainloop()