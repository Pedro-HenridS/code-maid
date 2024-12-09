from functions.getElement import getElement
from selenium.webdriver.common.by import By
from services.taskMaker import taskMaker
from services.driver import driver
from services.homepage import homepage


def findTask():

   browser = driver.browser

   print("chegou aqui 1")
   list_element = getElement(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/div/section[1]/div/div/ul/li[14]/div[3]/ul')

   itens_list_elements = list_element.find_elements(By.TAG_NAME, "li")

   for itens in itens_list_elements:
       link = itens_list_elements[itens].find_element(By.TAG_NAME, "a")

      
   print("chegou aqui 2")


   return 0

if __name__ == "__findTask__":
    findTask()