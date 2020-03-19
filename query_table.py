from db import connection

# https://docs.microsoft.com/en-us/sql/relational-databases/xml/basic-syntax-of-the-for-xml-clause?view=sql-server-ver15

# Query for Data
try:
    result = connection.execute('SELECT * FROM result FOR XML AUTO, ELEMENTS, ROOT')

    xml_str = list()

    for row in result:
        xml_str.append(row[0])

finally:
    connection.close()

xml_file = "".join(xml_str)

f = open("data/nr19_sprengel.xml", "w")
f.write(xml_file)
f.close()