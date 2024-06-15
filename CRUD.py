from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    # Property variables
    records_updated = 0
    records_matched = 0
    records_deleted = 0

    # Constructor to initialize the MongoDB
    def __init__(self, _username, _password, host, port, db, collection):
        """
        Initialize the MongoClient to access the MongoDB databases and collections.
        :param _username: MongoDB username
        :param _password: MongoDB password
        :param host: MongoDB host
        :param port: MongoDB port
        :param db: MongoDB database name
        :param collection: MongoDB collection name
        """
        userName = urllib.parse.quote_plus(_username)
        password = urllib.parse.quote_plus(_password)
        self.client = MongoClient(f'mongodb://{userName}:{password}@{host}:{port}/{db}?authSource=admin')
        self.dataBase = self.client[db]
        self.collection = self.dataBase[collection]

    #  Method to create a record in the animals collection
    def createRecord(self, data):
        if data:
            _insertValid = self.dataBase.animals.insert_one(data)
            #check the status of the inserted value 
            return True if _insertValid.acknowledged else False
	
        else:
            raise Exception("No document to save. Data is empty.")
    
   # Method to retrieve a record by its ObjectId
    def getRecordId(self, postId):
        _data = self.dataBase.find_one({'_id': ObjectId(postId)})
                                  
        return _data
    
# Method to retrieve records based on criteria
# Returns all records if no criteria is provided
# Example usage: shelter.getRecordCriteria({"breed": "Labrador Retriever"})
    def getRecordCriteria(self, criteria):
        if criteria:
            _data = self.dataBase.animals.find(criteria, {'_id' : 0})
                                 
        else:
            _data = self.dataBase.animals.find({},{'_id' : 0})
                                  
        return _data
    
    # Method to update records based on a query
    def updateRecord(self, query, newValue):
        if not query:
            raise Exception("No search criteria is present.")
        elif not newValue:
            raise Exception("No update value is present.")
        else:
            _updateValid = self.dataBase.animals.update_many(query, {"$set": newValue})
            self.records_updated = _updateValid.modified_count
            self.records_matched = _updateValid.matched_count

            return True if _updateValid.modified_count > 0 else False
    
   # Method to delete records based on a query
    def deleteRecord(self, query):
        if not query:
            raise Exception("No search criteria is present.")
        
        else:
            _deleteValid = self.dataBase.animals.delete_many(query)
            self.records_deleted = _deleteValid.deleted_count

            return True if _deleteValid.deleted_count > 0 else False      

