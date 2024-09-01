from argparse import ArgumentParser

parser = ArgumentParser(description='Excel -> DB: Read an Excel file and insert the data into a PostgreSQL table.')
parser.add_argument('--env-path', '-e', type=str, dest='envpath', help='The path to the .env file to load. Defaults to .env.')
parser.add_argument('--table-name', '-t', type=str, dest='tablename', help='The name of the table to insert the data into.')
parser.add_argument('--json-path', '-j', type=str, dest='jsonpath', help='The path of the JSON file with column data to load.')
parser.add_argument('--assume-yes', '-y', action='store_true', dest='assumeyes', help='Assume yes to prompts.')

group = parser.add_argument_group('XLSX Settings')
group.add_argument('--file-path', '-f', type=str, dest='filepath', help='The path to the Excel file to load.')
group.add_argument('--sheet-name', '-s', type=str, dest='sheetname', help='The name of the sheet to load, if the XLSX file has multiple sheets.')

group = parser.add_argument_group('Random ID Column Generation')
group.add_argument('--rand-col-name', '-c', type=str, dest='randcolname', help='The name of the column to generate ID values for.')
group.add_argument('--rand-col-length', '-l', type=int, dest='randcollength', help='The length of the random IDs to generate.')