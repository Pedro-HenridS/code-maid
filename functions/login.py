from selenium.webdriver.common.by import By
from services.AcessDB import *
from services.Driver import * 

def login(browser):
   browser = Driver.browser

   username = browser.find_element(By.ID, "username")
   senha = browser.find_element(By.ID, "password")
   login = browser.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]")

   reclaim = ["username","password"]
   itens = AcessDB.find("users", reclaim)

   username.send_keys(itens[0])
   senha.send_keys(itens[1])
   login.click()

   return 0

if __name__ == "__login__":
    login()