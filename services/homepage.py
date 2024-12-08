from functions.getElement import getElement
from selenium.webdriver.common.by import By

def homepage(browser, scroll=""):

   browser.get("https://ava3.cefor.ifes.edu.br/course/view.php?id=10014")

   if scroll != "":
      browser.execute_script(f"window.scroll(0, {scroll});")
      
   #browser.getElement(By.XPATH, '//*[@id="section-7"]/div[3]/ul', browser)

   return 0

if __name__ == "__homepage__":
    homepage()