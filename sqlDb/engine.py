import sqlalchemy as db
import os

USER = "fh01"
SUBDOMAIN = "dbfhproject"
PASSWORD = os.environ['DB_PASSWORD']
DATABASE = "myDatabase"

connection_string = f"mssql+pyodbc://{USER}@{SUBDOMAIN}:{PASSWORD}@{SUBDOMAIN}.database.windows.net:1433/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
engine = db.engine.create_engine(connection_string, echo=False)