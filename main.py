import os.path
from xml_project.sqlDB.config import CSV_FILE_NAME, XML_FILE_NAME
from xml_project.sqlDB.prepare import prepare_data
from xml_project.sqlDB.engine import engine
from xml_project.sqlDB.tables import result
from xml_project.sqlDB.xml import get_xml_file
from xml_project.existDB.exist import ExistClient
from xml_project.existDB.queries import relative_result_by_party_and_district


def main():
    # check if csv exists
    file_name = CSV_FILE_NAME
    project_path = os.path.join(os.path.dirname(__file__))
    file_path = os.path.join(project_path, "data", file_name)

    # prepare data for insert statement
    if os.path.isfile(file_path):
        data = prepare_data(file_path)
    else:
        print(f"{file_name} does not exist!")

    # create table
    try:
        result.create(engine)
    except Exception as e:
        print(e.args)

    # insert statement
    try:
        with engine.connect() as connection:
            connection.execute(result.insert(), data)
    except Exception as e:
        print(e.args)

    # query xml from database and export
    xml_file_name = XML_FILE_NAME
    get_xml_file(os.path.join(project_path, "data", xml_file_name))


def query_exist_db():
    # query from existDB
    try:
        client = ExistClient()
        rs = client.get(relative_result_by_party_and_district('GRUE', 8))
        return rs[0]
    except Exception as e:
        print(e.args)


if __name__ == "__main__":
    main()
    query_exist_db()
