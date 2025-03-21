from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()


user_table = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=False),
    Column("name", String(50))
)