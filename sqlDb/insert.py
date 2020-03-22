import re
import pandas as pd
from sqlDb.tables import result
from sqlDb.engine import engine

# read the data from csv
df = pd.read_csv("data/nr19_sprengel.csv", sep=";")

# replace nan with 0
df.fillna(0, inplace=True)

# cast col DISTRICT_CODE to int
df.astype({'DISTRICT_CODE': 'int32'})

# generate list of tuples
tup = list()

for index, row in df.iterrows():
    d = dict()
    d["id"] = index
    for i in range(0, 21):
        key = re.sub("[\s*\.\s*]", "", row.index[i])
        d[key] = row[i]
    tup.append(d)

# execute insert statement to SQL server
with engine.connect() as connection:
    connection.execute(result.insert(), tup)

