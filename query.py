from db import connection

s = "SELECT * FROM result FOR XML RAW"
query = connection.execute(s)

for row in query:
    print(row)

