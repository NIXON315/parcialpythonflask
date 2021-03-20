from src.models.basedb import DatabaseModel
from src import app
databaseModel = DatabaseModel()
class DatabaseController():
    def list(self):        
        data = databaseModel.lists()
        return data
    def create(self, databases):
        databaseModel.create(databases)
    def search(self, datab):
        data = databaseModel.listTables(datab)
        return data
