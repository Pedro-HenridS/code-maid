from functions.getElement import getElement
from selenium.webdriver.common.by import By
from services.driver import driver

def taskMaker():
    browser = driver.browser

    browser.implicitly_wait(10)
    question_div = getElement(By.CLASS_NAME, 'no-overflow')
    
    question_element = question_div.find_element(By.TAG_NAME, "p")
    question_text = question_element.text.strip()

    if not question_text:
      try:
         question_span = getElement(By.XPATH, '//*[@id="region-main"]/div/div[1]/div/div/p[1]/span')
         question_span_text = question_span.text
         print(question_span_text)
      except:
         question_span_text = "error"
         question_text = "error"

    print(question_text)
    print(question_span_text)
    

    return 0

if __name__ == "__taskMaker__":
    taskMaker()