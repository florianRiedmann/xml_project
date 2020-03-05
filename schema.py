from sqlalchemy import *

metadata = MetaData()

result = Table("result", metadata,
               Column("NUTS1", Integer),
               Column("NUTS2", Integer),
               Column("NUTS3", Integer),
               Column("DISTRICT_CODE", Integer),
               Column("T", Integer),
               Column("WV", Integer),
               Column("WK", Integer),
               Column("BZ", Integer),
               Column("SPR", Integer),
               Column("WBER", Integer),
               Column("ABG", Integer),
               Column("UNG", Integer),
               Column("OEVP", Integer),
               Column("SPOE", Integer),
               Column("FPOE", Integer),
               Column("NEOS", Integer),
               Column("JETZT", Integer),
               Column("GRUE", Integer),
               Column("KPOE", Integer),
               Column("WANDL", Integer),
               Column("BIER", Integer)
               )
