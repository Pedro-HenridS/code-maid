from selenium.webdriver.common.by import By
from services.Driver import Driver
import time

class Finder:

   browser = Driver.browser
   questions_links = []

   def findTask():

      list_element = Finder.browser.find_element(By.CSS_SELECTOR, '#section-13 > div.content > ul')

      itens_list_elements = list_element.find_elements(By.TAG_NAME, "li")

      links = 0

      qtd_itens = len(itens_list_elements)

      i = 0

      while i < qtd_itens:

         if i < 5:
            links = itens_list_elements[i].find_element(By.CSS_SELECTOR, f"#module-44034{i+1} > div > div > div:nth-child(2) > div.activityinstance > a")

         else:
            links = itens_list_elements[i].find_element(By.CSS_SELECTOR, f"#module-440358 > div > div > div:nth-child(2) > div.activityinstance > a")

         Finder.questions_links.append(links.get_attribute("href"))

         i = i + 1

      return Finder.questions_links

if __name__ == "__Finder__":
    Finder()