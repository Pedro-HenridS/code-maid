from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from services.Driver import Driver
from services.PromptMessage import Message

import time
import pyperclip

from functions.generativeResponse import generativeResponse


def taskMaker(link): # type: ignore
    browser = Driver.browser
    browser.get(link)

    message = Message 

    action = ActionChains(browser)
    
    edit_section = browser.find_element(By.CSS_SELECTOR, "#region-main > div > ul > li:nth-child(3) > a")
    edit_section_link = edit_section.get_attribute("href")
    
    #gera a resposta
    statement_text = browser.find_element(By.CSS_SELECTOR, "#region-main > div > div.box.py-3.generalbox > div > div > p:nth-child(1)").text

    res = generativeResponse(f"Gere um código Python condizente com o enunciado: '{statement_text}'. Responda mostrando apenas o código. Não coloque 'python' no início. A estrutura base deve ser a de main padrão, ou seja, 'def main():' e 'if __name__ == '__main__': main()'. O código deve ter quebras de linha e identação apropriadas.")

    #formata a resposta
    res = res.replace("```", "")
    res = res.replace("python", "")

    print(res)
   
    browser.get(edit_section_link)
    
    #Captura a seção de inserção de nome do ava3
    file_name = browser.find_element(By.CSS_SELECTOR, "#vpl_ide_input_newfilename")
    
    time.sleep(2)
    if file_name.is_displayed() == True:

         title_res = generativeResponse(f"Gere um nome de arquivo condizente com o enunciado: '{statement_text}', e coloque no final .py")
         
         file_name.send_keys(title_res + Keys.ENTER)

         message.fileCreated()
      

    else:
         message.fileExist()

    #seleciona o campo de texto
    ide_selector = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[4]/div/section/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]")

    for line in res.splitlines():

      pyperclip.copy(line)
      
      action.click(ide_selector).perform()

      if line == "if __name__ == '__main__':":
          action.key_down(Keys.BACKSPACE)\
          
      elif line == "main()":
          action.key_down(Keys.ENTER)\

      action.key_down(Keys.CONTROL)\
         .send_keys('v')\
         .key_up(Keys.CONTROL)\
         .key_down(Keys.RETURN)\
         .key_down(Keys.BACKSPACE)\
         .key_up(Keys.BACKSPACE)\
         .perform()

    save_element = browser.find_element(By.CSS_SELECTOR, "#vpl_ide_save")
    action.click(save_element).perform()

    run = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[4]/div/section/div/div[1]/div[1]/span[1]/a[3]")
    action.click(run).perform()
    
    time.sleep(20000)
    browser.back()

    return 0

if __name__ == "__taskMaker__":
    taskMaker()