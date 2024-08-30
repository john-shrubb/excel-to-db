# Excel to Database

The whole point of this project is to make a somewhat easy method of porting excel spreadsheets over to a database.

## Dependencies

- PostgreSQL (Tested on 16.4)
- Python 3.12

Set up a virtual environment and install the required packages with the script below:
```bash
python3 -m venv excel-to-db
source excel-to-db/bin/activate
pip install -r requirements.txt
```

## Dotenv

You may create a .env file in the root directory of this project with the following content for the database details:
```sh
db_host=IPADDRESS
db_port=PORTNUMBER
db_login=USERNAME
db_pass=PASSWORD
db_database=DATABASETOCONNECTTO
```

## Command Line Arguments

The CLI script when executed supports a number of arguments to entirely automate the process.
All file paths are relative to the CWD the script was executed in.

### `--env-path` | `-e`

Specified to a path to the .env file to use.

When not specified, the script will attempt to load a `.env` file in the CWD, falling back to manually prompting the user for DB details if this is not found.

### `--file-path` | `-f`

Specify a path to the Excel file to load.

### `--table-name` | `-t`

Specify the name of the table to attempt to insert data into.

### `--json-path` | `-j`

Specify the path of the JSON file to load with the column mappings already loaded. The JSON should be formatted like below:

```json
[
	{
		"columnName": "Forename",
		"dbColumnName": "forename",
		"columnType": "text"
	},
	{
		"columnName": "Surname",
		"dbColumnName": "surname",
		"columnType": "text"
	},
]
```

**Do not include random ID column in this JSON file, unless the random IDs are also being ported from the spreadsheet.**

### `--assume-yes` | `-y`

Attempt to answer yes to as many prompts as possible, such as the *View SQL before execution?* prompt.

Useful to pair with the rest of the command line arguments to entirely automate the script with no user input.

### `--rand-col-name` | `-c`

Specify a column to generate random IDs for. Useful for when everything is being ported to also attach an ID to each row.

Must be used in conjuntion with `-l` (See below).

### `--rand-col-length` | `-l`

Specify the length of the random IDs to generate. Can be any number from 1 to 255.

Note that using a small length and making the ID column a primary key may cause the script to crash.

## Example Data

This repository includes an example spreadsheet to experiment with.

Create a table in PostgreSQL with the following SQL statement:

```sql
CREATE TABLE example1 (
	forename text,
	surname text,
	dob date,
	adline1 text,
	postcode varchar(9),
	active boolean,
	creditscore smallint,
	id varchar(15)
);
```

Running python from the root of this repository and specifying database connection details in a .env file, using the following command should automatically insert the contents of the spreadsheet into a table.

```sh
python src/index.py -y -c INSERT_COL_NAME -l 15 -j ./exampleData/Example-1.json -f ./exampleData/Example-1.xlsx -t example1
```

**[Licensed under MIT.](./LICENSE)**