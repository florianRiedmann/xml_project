import pandas as pd
from tables import result
from db import connection

df = pd.read_csv("data/nr19_sprengel.csv", sep=";")
print(df.head())

l = [{'user_id': 1, 'email_address': 'jack@yahoo.com'},
     {'user_id': 1, 'email_address': 'jack@msn.com'},
     {'user_id': 2, 'email_address': 'www@www.org'},
     {'user_id': 2, 'email_address': 'wendy@aol.com'}]

ins = result.insert()
exe = connection.execute(ins)
