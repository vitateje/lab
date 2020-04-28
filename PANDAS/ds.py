import pandas as pd


# My personal ridiculous favorite: HTML table to DataFrame.
read_html = pd.read_html('/home/vitateje/Desktop/impact_code/PANDAS/teste.html')

excel_df = pd.read_excel('Book1.xls')

print(excel_df)
print(read_html)



