from selenium.webdriver.common.by import By
from services.Driver import Driver
import time
from functions.generativeResponse import generativeResponse

def taskMaker(link): # type: ignore
    browser = Driver.browser

    browser.get(link)

    statement_text = browser.find_element(By.CSS_SELECTOR, "#region-main > div > div.box.py-3.generalbox > div > div > p:nth-child(1)").text


    edit_section = browser.find_element(By.CSS_SELECTOR, "#region-main > div > ul > li:nth-child(3) > a")
    edit_section_link = edit_section.get_attribute("href")
    
    
    #gera o título e a resposta

    title_res = generativeResponse(f"Gere um nome de arquivo condizente com o enunciado: '{statement_text}', e coloque no final .py")
    res = generativeResponse(f"{statement_text}. Responda mostrando apensa o código. Não coloque ''' e nem precisa informar que a linguagem é python no início. A estrutura base deve ser a de main padrão, ou seja, def main(): return 0 if __name__ == '__main__': main() ")


    browser.get(edit_section_link)
    
    time.sleep(2)
    file_name = browser.find_element(By.CSS_SELECTOR, "#vpl_ide_input_newfilename")
    ok_button = browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/button[1]')
    
    file_name.send_keys(title_res)

    time.sleep(1)
    ok_button.click()

    browser.back()

    
    

    return 0

if __name__ == "__taskMaker__":
    taskMaker()