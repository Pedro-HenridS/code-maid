from services.driver import driver

def getElement(method, getText: str, browser=driver.browser):
    
    element = browser.find_element(method, getText)
    
    return element

if __name__ == "__getElement__":
    getElement()