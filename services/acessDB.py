from pymongo import MongoClient

class acessDB():
   
   def find(collection, reclaim): # type: ignore
      
         port = 27017

         client = MongoClient(f"mongodb://localhost:{port}/")
         db = client.get_database("auto_database")
         col = db.get_collection(collection)

         itens = []
         
         for i in range(len(reclaim)):
            search = list(col.find({}, {"_id": 0, reclaim[i]: 1}))

            for document in search:
               itens.append(document[reclaim[i]])

         return itens

   

if __name__ == "__acessDB__":
    acessDB()