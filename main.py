import os.path
from xml_project.sqlDB.config import CSV_FILE_NAME, XML_FILE_NAME
from xml_project.sqlDB.prepare import prepare_data
from xml_project.sqlDB.engine import engine
from xml_project.sqlDB.tables import result
from xml_project.sqlDB.xml import get_xml_file
from xml_project.existDB.exist import ExistClient
import xml_project.existDB.queries as query
from sqlalchemy.exc import SQLAlchemyError

CREATE_DB = False

def main():
    # check if csv exists
    file_name = CSV_FILE_NAME
    project_path = os.path.join(os.path.dirname(__file__))
    file_path = os.path.join(project_path, "data", file_name)

    # prepare data for insert statement
    if CREATE_DB:
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




if __name__ == "__main__":
    main()
    client = ExistClient()

    print("\nAbsolute Result for OEVP in District 5: ")
    [print(i) for i in client.get(query.absolut_votes_by_party_and_district('OEVP', 5))]

    print("\nRelative Result for GRUE in District 8: ")
    [print(i) for i in client.get(query.relative_result_by_party_and_district('GRUE', 8))]


    print("\nDistrict Relative Results ordered by Party: ")
    [print(i) for i in client.get(query.relative_results_ordered_by_party)]
    print("\nDistrict Relative Results ordered by Result: ")
    [print(i) for i in client.get(query.relative_results_ordered_by_result)]
    print("\nDistrict Voter Participation: ")
    [print(i) for i in client.get(query.participation)]
    print("\nDistrict Winner: ")
    [print(i) for i in client.get(query.winner)]

