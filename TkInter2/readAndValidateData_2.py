import tkinter as tk
import csv
import pandas as pd


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

    for row in range(1, len(data)):
        for col in range(len(data[0])):
            col_name = data[0][col]
            data_type = data_types.get(col_name, str)
            widget = grid.grid_slaves(row=row, column=col)[0]
            value = widget.get()
            try:
                data_type(value)
                widget.config(bg="white")
            except ValueError:
                widget.config(bg="red")

    # update_button['state'] = "normal"

def save_data():
    # Get the grid dimensions
    num_rows = len(data) - 1  # exclude header row
    num_cols = len(data[0])

    # Create an empty list to store the validated data
    validated_data = []

    # Iterate over the grid and validate each cell
    for row in range(1, num_rows + 1):  # start from row 1 to exclude header row
        row_data = []
        for col in range(num_cols):
            col_name = data[0][col]
            data_type = data_types.get(col_name, str)
            cell_widget = grid.grid_slaves(row=row, column=col)[0]
            cell_value = cell_widget.get()
            try:
                validated_value = data_type(cell_value)
                row_data.append(validated_value)
                cell_widget.config(bg="white")
            except ValueError:
                cell_widget.config(bg="red")
                return  # stop if there's an invalid value

        validated_data.append(row_data)

    # Convert the validated data into a pandas dataframe
    df = pd.DataFrame(validated_data, columns=data[0])

    # Save the dataframe to a file
    df.to_csv("validated_data.csv", index=False)

# Create a button to validate the data
validate_button = tk.Button(root, text="Validate", command=validate_data)
validate_button.pack(side=tk.BOTTOM)
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(side=tk.BOTTOM)
save_button['state']=tk.DISABLED

# Run the application
root.mainloop()
