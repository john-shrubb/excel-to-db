from dataclasses import dataclass

@dataclass
class ConnectionDetails:
	host: str
	port: int
	database: str
	user: str
	password: str
