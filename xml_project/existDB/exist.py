from pyexistdb import db
import xml_project.existDB.config as config


class ExistClient:

    def __init__(self):
        self.db = db.ExistDB(config.EXIST_URL, config.EXIST_USER, config.EXIST_PASSWORD)

    def get(self, query):
        try:
            resultId = self.db.executeQuery(query)
            hits = self.db.getHits(resultId)
            return [self.db.retrieve(resultId, x).data.decode('utf-8') for x in range(hits)]

        except db.ExistDBException as e:
            print("Exist Database Error:")
            print(e.args)