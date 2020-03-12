from db import connection

# https://docs.microsoft.com/en-us/sql/relational-databases/xml/basic-syntax-of-the-for-xml-clause?view=sql-server-ver15

s = "SELECT * FROM result FOR XML AUTO, TYPE, ELEMENTS, ROOT('Data')"

resultProxy = connection.execute(s)
rowProxy = resultProxy.fetchone()
rs = "".join(rowProxy)
connection.close()

f = open("data/nr19_sprengel.xml", "w")
f.write(rs)
f.close()