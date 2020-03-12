import sqlalchemy as db
from db import engine, connection

metadata = db.MetaData()

result = db.Table("result", metadata, db.Column("id", db.Integer, primary_key=True),
                  db.Column("NUTS1", db.String(10)),
                  db.Column("NUTS2", db.String(10)),
                  db.Column("NUTS3", db.String(10)),
                  db.Column("DISTRICT_CODE", db.String(10)),
                  db.Column("T", db.Integer),
                  db.Column("WV", db.Integer),
                  db.Column("WK", db.Integer),
                  db.Column("BZ", db.Integer),
                  db.Column("SPR", db.Integer),
                  db.Column("WBER", db.Integer),
                  db.Column("ABG",  db.Integer),
                  db.Column("UNG", db.Integer),
                  db.Column("OEVP", db.Integer),
                  db.Column("SPOE", db.Integer),
                  db.Column("FPOE", db.Integer),
                  db.Column("NEOS", db.Integer),
                  db.Column("JETZT", db.Integer),
                  db.Column("GRUE", db.Integer),
                  db.Column("KPOE", db.Integer),
                  db.Column("WANDL", db.Integer),
                  db.Column("BIER", db.Integer))

metadata.create_all(engine)
connection.close()