from cryptography.fernet import Fernet

def cryptography(key):

   cryptedPassword = Fernet(key)

   token = cryptedPassword.encrypt(key)
   
   cryptedPassword.decrypt(token)

   return cryptedPassword, token

if __name__ == "__cryptography__":
   cryptography()

