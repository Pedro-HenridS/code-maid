from cryptography.fernet import Fernet

def createCollections(database_name, client):
    
    db = client[database_name]
    collection_name = "users"
    
    status = bool()
    
    if collection_name not in db.list_collection_names():

      print(f"Criando a coleção '{collection_name}' no banco '{database_name}'...")

      collection = db[collection_name]

      username = str(input("Nome do usuário: "))
      password =  str(input("Senha do Usuário: "))
      token = str("")

      # Inserir um documento de exemplo
      collection.insert_one({
            "username": f"{username}",
            "password": f"{password}",
            "token": f"{token}"
         })
      
      print(f"Banco '{database_name}' e coleção '{collection_name}' configurados com sucesso.")

      status = True

    else:
      print(f"A coleção '{collection_name}' já existe no banco '{database_name}'.")
      status = True

    return status

if __name__ == "__createCollections__":
    createCollections()