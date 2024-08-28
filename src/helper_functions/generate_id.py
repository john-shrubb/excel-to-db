from random import randint

def generate_id(length: int, includeZero: bool = True) -> str:
	'''
	Generate a random ID of the specified length.

	:param length: The length of the ID to generate.
	:param includeZero: Whether to include zero in the generated ID. Defaults to True.
	'''
	if length < 1:
		raise ValueError('Must specify greater length than 0.')
	
	# Generate the ID

	id = []

	for i in range(length):
		id.append(str(randint(0 if includeZero else 1, 9)))

	return ''.join(id)