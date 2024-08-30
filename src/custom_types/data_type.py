from custom_types.data_type_enum import DataTypeEnum
from helper_functions.validate_float import validate_float
from helper_functions.stringify_value import stringify_value
from datetime import datetime
from helper_functions.parse_date import parse_date

class DataType:
	'''
	The DataType class is used to represent the data type values in a column should be converted to.

	Once defined, use the .parse() method to convert a value to the appropriate value which can be inserted into an SQL query.

	:param table_column_name: The name of the column in the table.
	:param db_column_name: The name of the column in the database.
	:param data_type: The data type the column should be converted to. Should be a value from the DataTypeEnum class, unless the type is an enumerator or other custom type in which pass a string as the name of the enumerator or type.
	:param possible_values: A list of possible values the column can take. If None, the column can take any value.
	'''
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
	
	def parse(self, value: str) -> str | int | float | datetime:
		match self.data_type:
			case DataTypeEnum.varchar | DataTypeEnum.char | DataTypeEnum.text:
				return str(value)
			case DataTypeEnum.int | DataTypeEnum.smallint | DataTypeEnum.bigint:
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid integer.')
				return int(value)
			case DataTypeEnum.numeric | DataTypeEnum.real | DataTypeEnum.double:
				if not validate_float(value):
					raise ValueError(f'Value {value} is not a valid float.')
				return float(value)
			case DataTypeEnum.date | DataTypeEnum.datetime:
				# Will handle both date and datetime
				return parse_date(value)
			case _:
				# Generally just assume the data type is an enum or something.
				return str(value)
