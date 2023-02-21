import tkinter as tk
import csv

# Create the main window
root = tk.Tk()

# Create the grid
grid = tk.Frame(root, borderwidth=1, relief="solid")
grid.pack()

# Read the data from the CSV file
with open('D:\Python\ETL Operations with Python\Files\CSVFileDataForLoadingOnGrid.csv') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Display the data in the grid
for i in range(len(data)):
    for j in range(len(data[i])):
        cell = tk.Entry(grid, validate="key")
        cell.insert(0, data[i][j])
        cell.grid(row=i, column=j)

# Define a function to validate the data
def validate_data():
    for widget in grid.winfo_children():
        if isinstance(widget, tk.Entry):
            value = widget.get()
            if not value.isdigit():
                widget.config(bg="red")
            else:
                widget.config(bg="white")

# Create a button to validate the data
validate_button = tk.Button(root, text="Validate", command=validate_data)
validate_button.pack(side=tk.BOTTOM)

# Run the application
root.mainloop()
