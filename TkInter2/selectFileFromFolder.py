import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Create a tkinter window
root = tk.Tk()

# Define a function to open the file dialog
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        # Display the first 5 rows of the DataFrame
        print(df.head())

# Create a button to browse for the file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Start the tkinter event loop
root.mainloop()
