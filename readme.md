# Excel to Database

The whole point of this project is to make a somewhat easy method of porting excel spreadsheets over to a database.

## Dependencies

- PostgreSQL (Tested on 16.4)
- Python 3.12

Install the library for interacting with xlsx sheets and PostgreSQL with the below command:
```sh
pip install openpyxl pyscopg2
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

**[Licensed under the MIT.](./LICENSE)**