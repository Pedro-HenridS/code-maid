from functions.getElement import getElement
from selenium.webdriver.common.by import By
from services.acessDB import *

def login(browser):
   username = getElement(By.ID, "username")
   senha = getElement(By.ID, "password")
   login = getElement(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]")

   reclaim = ["username","password"]
   itens = acessDB.find("users", reclaim)

   username.send_keys(itens[0])
   senha.send_keys(itens[1])
   login.click()

   return 0

if __name__ == "__login__":
    login()