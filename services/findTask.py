from functions.getElement import getElement
from selenium.webdriver.common.by import By

def findTask():
   ul_element = getElement(By.CLASS_NAME, "section img-text")
   li_element = ul_element.find_element(By.TAG_NAME, "li")

   print(len(li_element))

   return 0

if __name__ == "__findTask__":
    findTask()