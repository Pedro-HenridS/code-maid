from selenium.webdriver.common.by import By
from services.Driver import Driver
import time
from functions.generativeResponse import generativeResponse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def taskMaker(link): # type: ignore
    browser = Driver.browser
    browser.get(link)

    action = ActionChains(browser)

    statement_text = browser.find_element(By.CSS_SELECTOR, "#region-main > div > div.box.py-3.generalbox > div > div > p:nth-child(1)").text


    edit_section = browser.find_element(By.CSS_SELECTOR, "#region-main > div > ul > li:nth-child(3) > a")
    edit_section_link = edit_section.get_attribute("href")
    
    #gera a resposta
    res = generativeResponse(f"Gere um código Python condizente com o enunciado: '{statement_text}'. Responda mostrando apenas o código. Não coloque 'python' no início. A estrutura base deve ser a de main padrão, ou seja, 'def main():' e 'if __name__ == '__main__': main()'. O código deve ter quebras de linha e identação apropriadas.")

    res = res.replace("```", "")
    res = res.replace("python", "")
   
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

    #seleciona o: campo de texto; última linha; botão de save
    ide_selector = browser.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div[4]/div/section/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]")
    
    #action.click(ide_selector).perform()
    
    action.key_down(Keys.ENTER)\
      .send_keys(" ")\
      .key_up(Keys.ENTER)\
      .send_keys(" ")\
      .perform()

    #Coloca o texto no campo de texto, e configura o css para quebrar linha
    

    for line in res.splitlines():

      script = f"""
         var newDiv = document.createElement('div');
         var path = '/html/body/div[1]/div[3]/div/div[4]/div/section/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]'
         var ide = document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
         newDiv.class = 'ace_line';
         newDiv.innerText = '{line}';
         ide.appendChild(newDiv);
         """
      
      browser.execute_script(script)

    save_element = browser.find_element(By.CSS_SELECTOR, "#vpl_ide_save")
    save_element.click()
    time.sleep(500)
    
    time.sleep(2)
    browser.back()

    return 0

if __name__ == "__taskMaker__":
    taskMaker()