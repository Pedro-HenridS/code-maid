from selenium.webdriver.common.by import By
from services.Driver import Driver
import time
from functions.generativeResponse import generativeResponse
from selenium.webdriver.common.keys import Keys

def taskMaker(link): # type: ignore
    browser = Driver.browser

    browser.get(link)

    statement_text = browser.find_element(By.CSS_SELECTOR, "#region-main > div > div.box.py-3.generalbox > div > div > p:nth-child(1)").text


    edit_section = browser.find_element(By.CSS_SELECTOR, "#region-main > div > ul > li:nth-child(3) > a")
    edit_section_link = edit_section.get_attribute("href")
    
    
    #gera a resposta
    res = generativeResponse(f"{statement_text}. Responda mostrando apensa o código. Não coloque ''' e nem precisa informar que a linguagem é python no início. A estrutura base deve ser a de main padrão, ou seja, def main(): return 0 if __name__ == '__main__': main() ")


    browser.get(edit_section_link)

    file_name = browser.find_element(By.CSS_SELECTOR, "#vpl_ide_input_newfilename")
    
    time.sleep(2)
    if file_name.is_displayed() == True:

         title_res = generativeResponse(f"Gere um nome de arquivo condizente com o enunciado: '{statement_text}', e coloque no final .py")
         
         file_name.send_keys(title_res + Keys.ENTER)

         print("----------------------------------------------------------------")
         print("Arquivo do código criado!")
         print("----------------------------------------------------------------")

    else:
         print("----------------------------------------------------------------")
         print("Arquivo já existente!")
         print("----------------------------------------------------------------")

    
    ide_selector = browser.find_element(By.CSS_SELECTOR, "#vpl_file0 > div.ace_scroller > div.ace_content")

    browser.execute_script("arguments[0].textContent = arguments[1];", ide_selector, res)

    print("----------------------------------------------------------------")
    print(ide_selector.text)
    print("----------------------------------------------------------------")


    time.sleep(2)
    browser.back()

    
    

    return 0

if __name__ == "__taskMaker__":
    taskMaker()