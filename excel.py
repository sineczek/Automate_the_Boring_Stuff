import openpyxl, os


# syntax is outdated
workbook = openpyxl.load_workbook('example.xlsx') # otwieranie
print(type(workbook))

print(workbook.get_sheet_names())
sheet = workbook.get_sheet_by_name('Arkusz1')

cell = sheet['A1']
print(cell.value())



print(sheet.cell(row=1, column=2))