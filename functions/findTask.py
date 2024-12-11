from selenium.webdriver.common.by import By
from services.Driver import Driver

   
def findTask():
   browser = Driver.browser
   questions_links = []

   li_list = browser.find_elements(By.CLASS_NAME, 'activity')

   qtd_itens = len(li_list)

   i = 0

   while i < qtd_itens:

      try:

         links = li_list[i].find_element(By.CSS_SELECTOR, "#module-440343 > div > div > div:nth-child(2) > div.activityinstance > a")
         print(links.get_attribute("href"))

         questions_links.append(links.get_attribute("href"))
      except:
         pass

      i = i + 1

   return questions_links
   

if __name__ == "__findTask__":
    findTask()
  
  
  
  
  
  
   
   