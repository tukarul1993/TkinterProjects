import tkinter as tk
import pyodbc

def edit_data():
    # Connect to the database
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')
    cursor = conn.cursor()

    # Get the data from the form
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Execute an UPDATE statement to save the data to the database
    cursor.execute("UPDATE contacts SET email=?, phone=? WHERE name=?", (email, phone, name))
    conn.commit()
    cursor.close()
    conn.close()

root = tk.Tk()
root.title("Data Entry Form")

# Create labels and entry widgets for the form data
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="W")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, sticky="W")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=2, column=0, sticky="W")
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1)

# Create a button to save the data
edit_button = tk.Button(root, text="Save", command=edit_data)
edit_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
