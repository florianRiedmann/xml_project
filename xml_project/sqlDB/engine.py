import sqlalchemy as db
from xml_project.sqlDB.config import SQL_USER, SQL_SUB_DOMAIN, SQL_DATABASE, SQL_PASSWORD

# connection statement ms sql database
connection_string = f"mssql+pyodbc://{SQL_USER}@{SQL_SUB_DOMAIN}:{SQL_PASSWORD}@{SQL_SUB_DOMAIN}.database.windows.net:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

# initialize engine
engine = db.engine.create_engine(connection_string, echo=False)