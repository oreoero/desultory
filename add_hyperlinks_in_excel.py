import openpyxl

# Load the Excel workbook
workbook = openpyxl.load_workbook('example.xlsx')

# Set the hyperlink properties
url = 'https://www.example.com'
displayText = 'Example Website'

# Select the worksheet and table to insert the hyperlinks
worksheet = workbook.active
table_range = worksheet['A1':'E10']

# Loop through the cells in the table and create a hyperlink in each cell
for row in table_range:
    for cell in row:
        cell.value = displayText
        cell.hyperlink = url

# Save the Excel workbook
workbook.save('example.xlsx')
