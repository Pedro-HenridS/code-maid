from services.driver import driver
from database.database import database
from services.acessDB import *
from services.login import login
from services.homepage import homepage
from services.findTask import findTask




def main():

   browser = driver.browser
   db = database()
   
   if db:
      login(browser)
      homepage(browser, 45000)

      browser.implicitly_wait(5)
      findTask()
      
      input("Pressione Enter para fechar o navegador...")
    
   return 0

if __name__ == "__main__":
   main()