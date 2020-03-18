from db import connection

# https://docs.microsoft.com/en-us/sql/relational-databases/xml/basic-syntax-of-the-for-xml-clause?view=sql-server-ver15

# Query for Data
s = "SELECT * FROM result FOR XML AUTO, TYPE, ELEMENTS, ROOT('Data');"

resultProxy = connection.execute(s)
rowProxy = resultProxy.fetchone()
rs = "".join(rowProxy)

f = open("data/nr19_sprengel.xml", "w")
f.write(rs)
f.close()

# Query for Schema
s = "SELECT * FROM result FOR XML AUTO, ROOT('Data'), XMLSCHEMA;"

resultProxy = connection.execute(s)
rowProxy = resultProxy.fetchone()
rs = "".join(rowProxy)

f = open("data/nr19_sprengel.xsd", "w")
f.write(rs)
f.close()

connection.close()
