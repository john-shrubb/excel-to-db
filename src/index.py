import openpyxl
import argparse
from custom_types.data_type_enum import DataTypeEnum
from custom_types.data_type import DataType
from helper_functions.sql_identifier_check import ident_check
from helper_functions.generate_id import generate_id
from helper_functions.stringify_value import stringify_value

# Argument parsing stuff.
parser = argparse.ArgumentParser(prog='Excel to DB', description='Convert an Excel file to a Database.')
parser.add_argument('--file_path', type=str, help='The path to the Excel file to convert.')
parser.add_argument('-c', type=str, help='The name of the column to insert a randomm ID into.')
parser.add_argument('-l', type=int, help='The length of the random ID to insert.')

print('Excel -> DB v0.0.1')
print('------------------\n')

# Path will go from the current working directory when the script is executed.
file_path = ''

# Try to grab the file path from the arguments.
if not parser.parse_args().file_path:
	file_path = input('Enter the path to the XLSX file to convert: ')
else:
	file_path = parser.parse_args().file_path

rand_id_col_name = parser.parse_args().c
rand_id_col_length = parser.parse_args().l

if not rand_id_col_name or not rand_id_col_length:
	print('Random ID column name and length were not provided. Will not insert random IDs.\nExecute with the -h flag for help.')
else:
	print(f'Random ID column name: {rand_id_col_name}')
	print(f'Random ID column length: {rand_id_col_length}')

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

# Get an array of the data types from the enum
valid_data_types = [data_type.value for data_type in DataTypeEnum]

data_types : list[DataType] = []

# The more user interface heavy portion of the app.
# Prompts the user for the data type of each column.
print('Please enter the desired data type for each column.\nEnter /? when entering data type to view a list of valid data types.')
for i in range(1, max_columns + 1):
	print(f'Column {i}: {sheet_object.cell(row=1, column=i).value}')
	while True:
		db_column_name = input('Enter the name of this column in the database: ').strip()
		if not ident_check(db_column_name):
			print('Invalid column name.')
			continue

		# Prevent duplicate column names.
		for data_type in data_types:
			if data_type.db_column_name == db_column_name:
				print('Column already exists.')
				continue
		
		# Grab the data type from user.
		data_type_name = input('Enter data type: ').strip().lower()

		# Display a help message.
		if data_type_name == '/?':
			print('Valid data types:')
			for data_type in DataTypeEnum:
				print(data_type.value)
			print('If you are entering a custom data type (For example an enumerator) enter the name of the type.')
			continue

		# Check that the data type is a valid type of identifier.
		if not ident_check(data_type_name):
			print('Invalid data type name.')
			continue

		# If the data type is valid, add it to the data_types dictionary.
		else:
			data_type = DataType(
				table_column_name = str(sheet_object.cell(row=1, column=i).value),
				db_column_name = db_column_name,
				data_type = DataTypeEnum[data_type_name]
			)
			data_types.append(data_type)
			break

# Print out the data types. (DEBUG)
for data_type in data_types:
	print(f'{data_type.table_column_name} -> {data_type.db_column_name} -> {data_type.data_type}')

# Also debug - Read the first rows

for row in range(2, sheet_object.max_row + 1):
	to_insert : dict[str, str]= {}
	to_insert[rand_id_col_name] = stringify_value(generate_id(rand_id_col_length))
	for column in range(1, max_columns + 1):
		# Key is the column name, value is the value to insert.
		data_type = data_types[column - 1]

		# DEBUG - Print the data type and the parsed value.
		print(f'{data_type.data_type} -> {data_type.parse(str(sheet_object.cell(row=row, column=column).value))}')

		# Add the value to the dictionary.
		to_insert[data_type.db_column_name] = data_type.parse(str(sheet_object.cell(row=row, column=column).value))

	print(
		f'INSERT INTO table_name ({', '.join(to_insert.keys())}) VALUES ({', '.join(to_insert.values())});'
	)