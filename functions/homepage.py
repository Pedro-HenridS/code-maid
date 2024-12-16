def homepage(browser, scroll=""):

   browser.get("https://ava3.cefor.ifes.edu.br/course/view.php?id=10014")
   
   if scroll != "":
      browser.execute_script(f"window.scroll(0, {scroll});")

   return 0

if __name__ == "__homepage__":
    homepage()