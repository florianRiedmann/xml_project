import re
import pandas as pd
from tables import result
from db import connection

# read the data from csv
df = pd.read_csv("data/nr19_sprengel.csv", sep=";")

# parse the data into the right structure
l = list()

for index, row in df.iterrows():
    d = dict()
    d["id"] = index
    for i in range(0,21):
        key = re.sub("[\.\s*]", "", row.index[i])
        if key == "DISTRICT_CODE":
            d[key] = str(row[i])
        else:
            d[key] = row[i]
    l.append(d)

# execute insert statement to SQL server
exe = connection.execute(result.insert(), l)
