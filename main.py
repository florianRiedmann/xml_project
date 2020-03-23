import os.path
from xml_project.sqlDB.config import CSV_FILE_NAME, XML_FILE_NAME
from xml_project.sqlDB.prepare import prepare_data
from xml_project.sqlDB.engine import engine
from xml_project.sqlDB.tables import result
from xml_project.sqlDB.xml import get_xml_file
from xml_project.existDB.exist import ExistClient
from xml_project.existDB.queries import winner, participation
from sqlalchemy.exc import SQLAlchemyError


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
    print("CREATE TABLE")
    try:
        result.create(engine)
    except SQLAlchemyError as e:
        print("Error: There is already an object named 'result'!")

    print("INSERT INTO")
    # insert statement
    try:
        with engine.connect() as connection:
            connection.execute(result.insert(), data)
    except SQLAlchemyError:
        print("Error: Cannot insert duplicate key in object!")

    # query xml from database and export
    xml_file_name = XML_FILE_NAME
    get_xml_file(os.path.join(project_path, "data", xml_file_name))


def query_winner_nr19():
    # query from existDB
    try:
        client = ExistClient()
        rs = client.get(winner)
        return rs
    except Exception as e:
        print("SQL Database Error:")
        print(e.args)


def query_part_nr19():
    # query from existDB
    try:
        client = ExistClient()
        rs = client.get(participation)
        return rs
    except Exception as e:
        print("SQL Database Error:")
        print(e.args)


if __name__ == "__main__":
    main()
    print("\nDistrict Winner: ")
    [print(i) for i in query_winner_nr19()]
    print("\nDistrict Voter Participation: ")
    [print(i) for i in query_part_nr19()]

