from xml_project.sqlDB.engine import engine

stmt = """DECLARE @header VARCHAR(50);
DECLARE @namespace VARCHAR(50);
DECLARE @x XML

SET @header = '<?xml version="1.0" encoding="UTF-8"?>';
SET @namespace = '<root xmlns="http://nr19.org/nr19_schema">';
SET @x = (
SELECT *
FROM result
FOR XML PATH ('result'), ROOT ('root'))

SELECT CAST(CONCAT(@header, REPLACE(CAST(@x AS NVARCHAR(MAX)), '<root>', @namespace)) AS NTEXT);"""


def get_xml_file(path):
    try:
        # raw DBAPI connection
        connection = engine.raw_connection()
        cursor = connection.cursor()
        result = cursor.execute(stmt)

        xml_str = list()

        for row in result:
            xml_str.append(row[0])

    finally:
        cursor.close()

    # concat row strings
    xml_file = "".join(xml_str)

    # save query to a file
    f = open(path, "w")
    f.write(xml_file)
    f.close()
