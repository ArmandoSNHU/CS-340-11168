from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, collection):
        """
        Initialize the MongoClient to access the MongoDB databases and collections.
        :param user: MongoDB username
        :param password: MongoDB password
        :param host: MongoDB host
        :param port: MongoDB port
        :param db: MongoDB database name
        :param collection: MongoDB collection name
        """
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[collection]

    def create(self, data):
        """
        Insert a document into the collection.
        :param data: A dictionary containing the data to be inserted.
        :return: True if insert is successful, False otherwise.
        """
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred while inserting: {e}")
                return False
        else:
            raise ValueError("data parameter is empty")

    def read(self, query):
        """
        Query for documents from the collection.
        :param query: A dictionary containing the query parameters.
        :return: A list of documents matching the query, or an empty list if none found.
        """
        if query:
            try:
                documents = self.collection.find(query)
                return list(documents)
            except Exception as e:
                print(f"An error occurred while querying: {e}")
                return []
        else:
            raise ValueError("query parameter is empty")

# Example usage of the module
if __name__ == "__main__":
    # Connection variables
    USER = 'aacuser'
    PASS = 'snhu123'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 30464
    DB = 'AAC'
    COL = 'animals'

    # Instantiate the AnimalShelter class
    shelter = AnimalShelter(USER, PASS, HOST, PORT, DB, COL)
    
    # Example data to insert
    example_data = {
        "age_upon_outcome": "1 year",
        "animal_id": "A123456",
        "animal_type": "Dog",
        "breed": "Labrador Retriever",
        "color": "Black",
        "date_of_birth": "2020-01-01",
        "datetime": "2021-01-01 12:34:56",
        "monthyear": "2021-01",
        "name": "Rex",
        "outcome_subtype": "",
        "outcome_type": "Adoption",
        "sex_upon_outcome": "Neutered Male",
        "location_lat": 30.628,
        "location_long": -97.678,
        "age_upon_outcome_in_weeks": 52
    }

    # Insert example data
    insert_success = shelter.create(example_data)
    print(f"Insert successful: {insert_success}")

    # Query example
    query = {"animal_type": "Dog"}
    results = shelter.read(query)
    for doc in results:
        print(doc)

