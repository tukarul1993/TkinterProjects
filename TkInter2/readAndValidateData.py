import tkinter as tk
import csv


# Define the data types of each column
data_types = {'Id': int, 'Name': str, 'Age': int}

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
    for col in range(len(data[0])):
        col_name = data[0][col]
        data_type = data_types.get(col_name, str)
        for widget in grid.grid_slaves(column=col):
            value = widget.get()
            try:
                data_type(value)
                widget.config(bg="white")
            except ValueError:
                widget.config(bg="red")

# Create a button to validate the data
validate_button = tk.Button(root, text="Validate", command=validate_data)
validate_button.pack(side=tk.BOTTOM)

# Run the application
root.mainloop()
