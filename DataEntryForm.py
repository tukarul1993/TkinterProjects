import pandas as pd

# Load data from different sheets in an Excel workbook
with pd.ExcelFile('Book1.xlsx') as xlsx:
    df1 = pd.read_excel(xlsx, 'Sheet1')
    df2 = pd.read_excel(xlsx, 'Sheet2')
    df3 = pd.read_excel(xlsx, 'Sheet3')

# You can now use the dataframes df1, df2, and df3 for further processing or analysis

print(df3)