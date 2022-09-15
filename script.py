import openpyxl

# Open the file
path = "input.xlsx"  # please specific file path

wb = openpyxl.load_workbook(path)
sheet = wb.active

# Get the working column
working_col = 0

for col in range(1, sheet.max_column+1):
    if (sheet.cell(row=1, column=col).value == "Kroužky"):
        working_col = col
        break

print("The working coulm is: ", working_col)

# Create a camp collection
camps = []
for row in range(2, sheet.max_row+1):
    cell = sheet.cell(row=row, column=working_col).value
    if (cell != None):
        cell_camps = cell.split(";")
        for value in cell_camps:
            if value not in camps and value != "":
                camps.append(value)

print(camps)
