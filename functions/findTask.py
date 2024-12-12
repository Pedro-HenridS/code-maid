from selenium.webdriver.common.by import By
from services.Driver import Driver

from services.PromptMessage import Message

   
def findTask():
   browser = Driver.browser
   questions_links = []

   li_list = browser.find_elements(By.CLASS_NAME, 'activity')
   qtd_itens = len(li_list)

   i = 0

   while i < qtd_itens:

      try:
         checkbox = li_list[i].find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[3]/div/section[1]/div/div/ul/li[8]/div[3]/ul/li[23]/div/div/div[2]/div[2]/form/div/button")
         
         if "Concluído(s):" in checkbox.get_attribute("alt"):
               Message.taskDone()

               break

         elif "Não concluído(s):" in checkbox.get_attribute("alt"):
            links = li_list[i].find_element(By.CSS_SELECTOR, "#module-440343 > div > div > div:nth-child(2) > div.activityinstance > a")

            print(links.get_attribute("href"))

            questions_links.append(links.get_attribute("href"))

      except:
         pass

      i = i + 1

   return questions_links
   

if __name__ == "__findTask__":
    findTask()
  
  
  
  
  
  
   
   