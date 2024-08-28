# Exercpt from Google:
# SQL identifiers and key words must begin with a letter ( a - z , but also letters with diacritical marks and non-Latin letters) or an underscore ( _ ). Subsequent characters in an identifier or key word can be letters, underscores, digits ( 0 - 9 ), or dollar signs ( $ ).

def ident_check(value : str) -> bool:
	"""
	Checks if a string is a valid SQL identifier.
	"""
	# Check that the identifier begins with a letter
	if not value[0].isalpha() and not value[0] == '_':
		return False
	
	# Check through each character in the identifier
	for i in range(1, len(value)):
		if (not value[i].isalpha() and # Is an alphabetical character
	  		not value[i] == '_' and # Or is an underscore
			not value[i].isdigit() and # Or is a digit
			not value[i] == '$' # Or is a dollar sign
		):
			return False
	return True
# Test cases
print(ident_check("valid_identifier"))  # True
print(ident_check("_underscore"))  # True
print(ident_check("123"))  # False
print(ident_check("$dollar$"))  # True
print(ident_check("invalid-identifier"))  # False