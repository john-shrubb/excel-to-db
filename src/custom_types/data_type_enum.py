from enum import Enum

class DataTypeEnum(Enum):
	smallint = 'smallint'
	int = 'int'
	bigint = 'bigint'
	# I can't really validate this, will just need to assume that the value is valid if it parses as a float.
	numeric = 'numeric'
	real = 'real'
	double = 'double'
	boolean = 'boolean'
	date = 'date'
	datetime = 'datetime'
	varchar = 'varchar'
	# Be careful when using char.
	# Going under the defined length of a char type will result in the value being padded with spaces with no warning or error.
	char = 'char'
	text = 'text'
