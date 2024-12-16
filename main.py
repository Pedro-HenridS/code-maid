from services.Driver import Driver
from services.AcessDB import *

from database.database import database

from functions.findTask import findTask
from functions.login import login
from functions.homepage import homepage
from functions.taskMaker import taskMaker

import time

def main():

   browser = Driver.browser
   db = database()
   
   if db:
      login(browser)
      homepage(browser, 13450)
      

      time.sleep(2000)
      links = findTask()
      
      for link in links:
         taskMaker(link)
      
      input("Pressione Enter para fechar o navegador...")
    
   return 0

if __name__ == "__main__":
   main()