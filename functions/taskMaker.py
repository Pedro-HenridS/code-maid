from selenium.webdriver.common.by import By
from services.Driver import Driver
import time

def taskMaker(link): # type: ignore
    browser = Driver.browser

    browser.get(link)

    time.sleep(3)

    statement_text = browser.find_element(By.CSS_SELECTOR, "#region-main > div > div.box.py-3.generalbox > div > div > p:nth-child(1)").text
    
    print("------------------------------------------------------------")
    print(statement_text)
    print("------------------------------------------------------------")



    browser.back()

    
    

    return 0

if __name__ == "__taskMaker__":
    taskMaker()