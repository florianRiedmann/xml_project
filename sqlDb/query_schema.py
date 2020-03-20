from db import connection

# Query for Schema and Data
try:
    result = connection.execute('SELECT * FROM result FOR XML AUTO, XMLSCHEMA, ELEMENTS, ROOT')

    xml_str = list()

    for row in result:
        xml_str.append(row[0])

finally:
    connection.close()

xml_schema = "".join(xml_str)

f = open("data/nr19_sprengel_inline_schema.xml", "w")
f.write(xml_schema)
f.close()