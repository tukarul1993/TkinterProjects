import tkinter as tk
import pyodbc

def submit_form():
    # collect values from the form entries
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # clear form entries
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

    # insert the data into the database
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=ITLNB619;'
                            'DATABASE=SSIS_Practice;'
                            'UID=sa;'
                            'PWD=admin@123')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    cursor.close()
    conn.close()

    print("Data saved successfully!")

root = tk.Tk()
root.title("Data Entry Form")

# create form labels
name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root, text="Email:")
phone_label = tk.Label(root, text="Phone:")

# create form entries
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_entry = tk.Entry(root)

# create submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)

# place form labels and entries on the window
name_label.grid(row=0, column=0, sticky="E")
name_entry.grid(row=0, column=1)
email_label.grid(row=1, column=0, sticky="E")
email_entry.grid(row=1, column=1)
phone_label.grid(row=2, column=0, sticky="E")
phone_entry.grid(row=2, column=1)
submit_button.grid(row=3, column=1, pady=10)

root.mainloop()
