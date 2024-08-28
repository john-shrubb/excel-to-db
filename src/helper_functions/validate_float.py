def validate_float(value: str) -> bool:
	'''
	Validate that a value is a valid float.
	'''
	try:
		float(value)
		return True
	except:
		return False