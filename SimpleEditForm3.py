import pyodbc
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

# Connect to the database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Execute an SQL statement to select all data from a table
cursor.execute('SELECT * FROM test')

# Fetch all rows of data and store them in a list of tuples
data = cursor.fetchall()

# Create a standard item model to populate the table view
model = QStandardItemModel(len(data), len(data[0]))

# Set the headers for the table view
model.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

# Populate the table view with data from the database
for row_num, row_data in enumerate(data):
    for col_num, col_data in enumerate(row_data):
        item = QStandardItem(str(col_data))
        model.setItem(row_num, col_num, item)

# Create a table view and set the model
view = QTableView()
view.setModel(model)

# Allow editing of the table view
view.setEditTriggers(QTableView.DoubleClicked)

# Create a main window and set the table view as the central widget
window = QMainWindow()
window.setCentralWidget(view)

# Show the main window
window.show()

# Start the application event loop
app = QApplication([])
app.exec_()

# Save changes to the database
for row_num in range(model.rowCount()):
    row_data = []
    for col_num in range(model.columnCount()):
        item = model.item(row_num, col_num)
        row_data.append(item.text())
    cursor.execute('UPDATE test SET Name=?, Address=?, Salary=? WHERE ID=?',
                   (row_data[0], row_data[1], row_data[2], row_num + 1))
conn.commit()

# Close the database connection
conn.close()
