from msgspec import Struct

class Config_Database(Struct):
    dsn: str

class Config(Struct):
    database: Config_Database
    token: str
    prefix: str | list[str]
    extensions: list[str]
