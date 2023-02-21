import tkinter as tk
import pyodbc

def show_data():
    # Connect to the database
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve data from the database
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Clear any previous data from the window
    for widget in data_frame.winfo_children():
        widget.destroy()

    # Create column headers
    tk.Label(data_frame, text="Name", font=("TkDefaultFont", 10, "bold")).grid(row=0, column=0, sticky="W")
    tk.Label(data_frame, text="Email", font=("TkDefaultFont", 10, "bold")).grid(row=0, column=1, sticky="W")
    tk.Label(data_frame, text="Phone", font=("TkDefaultFont", 10, "bold")).grid(row=0, column=2, sticky="W")

    # Add rows of data to the window
    for i, row in enumerate(rows):
        tk.Label(data_frame, text=row[0]).grid(row=i+1, column=0, sticky="W")
        tk.Label(data_frame, text=row[1]).grid(row=i+1, column=1, sticky="W")
        tk.Label(data_frame, text=row[2]).grid(row=i+1, column=2, sticky="W")

root = tk.Tk()
root.title("Data Entry Form")

# Create a button to show the data
show_data_button = tk.Button(root, text="Show Data", command=show_data)
show_data_button.pack()

# Create a frame to hold the data
data_frame = tk.Frame(root)
data_frame.pack()

root.mainloop()
