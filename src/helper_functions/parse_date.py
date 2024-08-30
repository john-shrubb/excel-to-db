from datetime import datetime

def parse_date(date_str : str) -> datetime:
	'''
	Parse a date string into a datetime format.

	Formats accepted are:
	- YYYY-MM-DD
	- YYYY-NN-DD HH:MM:SS

	:param date_str: The date string to parse.
	'''
	
	if ' ' in date_str:
		return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
	else:
		return datetime.strptime(date_str, '%Y-%m-%d')