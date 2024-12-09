from pymongo import MongoClient
import os

from functions.createCollections import createCollections

def database():
   
    db_folder = os.path.join(os.getcwd(), "database")
    port = 27017
    database_name = "auto_database"
    
    client = MongoClient(f"mongodb://localhost:{port}/")

    status = createCollections(database_name, client)

    client.close()


    return status

if __name__ == "__database__":
    database()