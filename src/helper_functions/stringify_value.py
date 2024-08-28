def stringify_value(value: str) -> str:
	"""
	Convert a value into a string format which can be passed into an SQL query.
	"""
	nvalue = value.split('')
	nvalue.append('\'')
	nvalue.insert(0, '\'')
	return ''.join(nvalue)