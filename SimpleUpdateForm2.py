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

        edit_button = ttk.Button(frame, text="Edit", command=lambda row=i+1: edit_row(row))
        edit_button.grid(row=i+1, column=j+1)

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

# Define a function to handle the "Edit" button click
def edit_row(row):
    # Get the values of the selected row from the grid
    values = []
    for child in frame.winfo_children():
        if isinstance(child, ttk.Entry) and int(child.grid_info()['row']) == row:
            values.append(child.get())

    # Open a new window with a form to edit the selected row
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Row")

    # Add labels and entry fields for each column
    headers = ['Column 1', 'Column 2', 'Column 3']
    for i, header in enumerate(headers):
        label = ttk.Label(edit_window, text=header)
        label.grid(row=i, column=0)
        entry = ttk.Entry(edit_window, width=10)
        entry.insert(0, values[i])
        entry.grid(row=i, column=1)

    # Add a "Save" button to update the row in the database
    save_button = ttk.Button(edit_window, text="Save", command=lambda: save_row(row, headers, edit_window))
    save_button.grid(row=len(headers), column=0, columnspan=2)

# Define a function to update the database with the edited row
def save_row(row, headers, edit_window):
    # Get the edited values from the form
    values = [edit_window.winfo_children()[i].get() for i in range(len(headers))]

    # Execute SQL query to update the corresponding row in the database
    cursor = conn.cursor()
    update_query = f"UPDATE test SET "
    for i, header in enumerate(headers):
        update_query += f"{header}='{values[i]}'"
        if i < len(headers) - 1:
            update_query += ", "
    update_query += f" WHERE ID={row}"
    cursor.execute(update_query)
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