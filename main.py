from services.Driver import Driver
from services.AcessDB import *
from services.Finder import Finder

from database.database import database

from functions.login import login
from functions.homepage import homepage
from functions.taskMaker import taskMaker

def main():

   browser = Driver.browser
   db = database()
   
   if db:
      login(browser)
      homepage(browser, 13450)
      
      links = Finder.findTask()
      
      for link in links:
         taskMaker(link)
      
      input("Pressione Enter para fechar o navegador...")
    
   return 0

if __name__ == "__main__":
   main()