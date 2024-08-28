from data_type_enum import DataTypeEnum
from helper_functions.validate_float import validate_float
from helper_functions.stringify_value import stringify_value
import datetime

class DataType:
	"""
	The DataType class is used to represent the data type values in a column should be converted to.

	Once defined, use the .parse() method to convert a value to the appropriate value which can be inserted into an SQL query.

	:param table_column_name: The name of the column in the table.
	:param db_column_name: The name of the column in the database.
	:param data_type: The data type the column should be converted to. Should be a value from the DataTypeEnum class, unless the type is an enumerator or other custom type in which pass a string as the name of the enumerator or type.
	:param possible_values: A list of possible values the column can take. If None, the column can take any value.
	"""
	def __init__(
		self,
		table_column_name: str,
		db_column_name: str,
		data_type : DataTypeEnum | str,
		possible_values: list[str] | None = None
	):
		self.table_column_name = table_column_name
		self.db_column_name = db_column_name
		self.data_type = data_type
		self.possible_values = possible_values

	def parse(self, value : str, autoCorrect : bool = False) -> str:
		"""
		Parse a value into a form which can be passed into a database. Will also perform some validation to ensure that value doesn't violate DB constraints.
		
		For example: A smallint can only take values between -32768 and 32767.

		When passing in a date, use format YYYY-MM-DD.

		:param value: The value to parse.
		:param autoCorrect: If True, will attempt to correct the value if it is invalid. If False, will raise an error if the value is invalid.
		"""
		# Match with all possible data types.
		# TODO: Make validation more modular.
		match DataTypeEnum:
			case DataTypeEnum.smallint:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid integer.')
				
				int_value = int(value)

				# Range check to ensure that the value is within the range of a smallint.
				if int_value < -32768 or int_value > 32767:
					raise ValueError(f'Value {value} is not within the range of a smallint.')

				return value
			case DataTypeEnum.int:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid integer.')
				
				int_value = int(value)

				# Range check - int
				if int_value < -2147483648 or int_value > 2147483647:
					raise ValueError(f'Value {value} is not within the range of a smallint.')

				return value
			case DataTypeEnum.bigint:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid integer.')
				
				int_value = int(value)

				# Range check - bigint
				if int_value < -9223372036854775808 or int_value > 9223372036854775807:
					raise ValueError(f'Value {value} is not within the range of a bigint.')

				return value
			case DataTypeEnum.numeric:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid float.')

				return value
			case DataTypeEnum.real:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid float.')

				# Validate number of decimal places.
				if len(value.split('.')[1]) > 6:
					if not autoCorrect:
						raise ValueError(f'Value {value} has more than 6 decimal places.')
					else:
						value = str(round(float(value), 6))
				
				return value
			case DataTypeEnum.double:
				# Validate the value
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid float.')

				# Validate number of decimal places.
				if len(value.split('.')[1]) > 15:
					if not autoCorrect:
						raise ValueError(f'Value {value} has more than 15 decimal places.')
					else:
						value = str(round(float(value), 15))

				return value
			case DataTypeEnum.boolean:
				# Validate the value
				if value.lower() not in ['true', 'false']:
					raise ValueError(f'Value {value} is not a valid boolean.')

				return stringify_value(value.lower())
			case DataTypeEnum.date:
				date_list = value.split('-')
				for date_part in date_list:
					if not date_part.isdigit():
						raise ValueError(f'Value {value} is not a valid date.')
				year = int(date_list[0])
				month = int(date_list[1])
				day = int(date_list[2])

				try:
					datetime.datetime(year, month, day) # type: ignore
				except ValueError:
					raise ValueError(f'Value {value} is not a valid date.')
				
				return stringify_value(value)
			case DataTypeEnum.datetime:
				# YYYY-MM-DD HH:MM:SS
				# 2021-02-03 00:00:00
				date_list = value
				delimiters = ['-', ' ', ':']

				# Remove all delimiters.
				for char in delimiters:
					date_list = ' '.join(date_list.split(char))

				# Split the date into individual parts.
				date_list = date_list.split(' ')

				if len(date_list) != 6:
					raise ValueError(f'Value {value} is not a valid datetime.')

				# Assign individual variables.
				year = int(date_list[0])
				month = int(date_list[1])
				day = int(date_list[2])
				hour = int(date_list[3])
				minute = int(date_list[4])
				second = int(date_list[5])

				# Validate the date.
				try:
					datetime.datetime(year, month, day, hour, minute, second) # type: ignore
				except ValueError:
					raise ValueError(f'Value {value} is not a valid datetime.')

				return stringify_value(value)
			case DataTypeEnum.varchar:
				if self.possible_values and not value in self.possible_values:
					raise ValueError(f'Value {value} is not a valid value for this column.')
				
				return stringify_value(value)
			case DataTypeEnum.char:
				if self.possible_values and not value in self.possible_values:
					raise ValueError(f'Value {value} is not a valid value for this column.')

				return stringify_value(value)
			case DataTypeEnum.text:
				if self.possible_values and not value in self.possible_values:
					raise ValueError(f'Value {value} is not a valid value for this column.')

				return stringify_value(value)
			case _:
				# Assume the data type is a custom type, e.g: an enumerator.
				if self.possible_values and not value in self.possible_values:
					raise ValueError(f'Value {value} is not a valid value for this column.')
				return stringify_value(value)