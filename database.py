import sqlalchemy
# https://docs.sqlalchemy.org/en/13/core/engines.html
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#driver-files

USER = "fh01"
SUBDOMAIN = "dbfhproject"
PASSWORD = "Kilbi1991"
DATABASE = "myDatabase"

connection_string = f"mssql+pyodbc://{USER}@{SUBDOMAIN}:{PASSWORD}@{SUBDOMAIN}.database.windows.net:1433/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
engine = sqlalchemy.engine.create_engine(connection_string, echo=True)
engine.connect()
