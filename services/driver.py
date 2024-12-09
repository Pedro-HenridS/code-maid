from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Driver():
   
   def driver():
      driver_path = "C:\\Users\\Pichau\\.wdm\\drivers\\chromedriver\\win64\\128.0.6613.137\\chromedriver-win32\\chromedriver.exe"
      chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

      chrome_options = Options()
      chrome_options.binary_location = chrome_path

      service = Service(driver_path)
      driver = webdriver.Chrome(service=service, options=chrome_options)
      driver.get("https://ava3.cefor.ifes.edu.br")
      
      return driver
   
   browser = driver() 

if __name__ == "__driver__":
    Driver()