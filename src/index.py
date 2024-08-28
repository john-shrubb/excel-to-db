import openpyxl

print('Excel -> DB v0.0.1')
print('-------------------------')
# Path will go from the current working directory when the script is executed.
file_path = input('Enter path to XLSX file: ')

# Load the workbook
wb = 0

# Catch if the workbook doesn't exist.
try:
	wb = openpyxl.load_workbook(file_path)
except:
	print('Error opening this file.')
	exit()


# Get active sheet
sheet_object = wb.active

if sheet_object == None:
	raise TypeError('No active sheet found.')
	exit()

# Get the amount of columns.
max_columns = sheet_object.max_column
