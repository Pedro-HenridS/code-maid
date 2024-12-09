from selenium.webdriver.common.by import By
from services.Driver import Driver
import time

def taskMaker(link): # type: ignore
    browser = Driver.browser

    browser.get(link)

    time.sleep(4)



    browser.back()

    
    

    return 0

if __name__ == "__taskMaker__":
    taskMaker()