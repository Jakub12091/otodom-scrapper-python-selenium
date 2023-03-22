from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach', True)

from menu import poop_up


def zebranie_linków(lista_kryteriów):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    linki =[]
    url = lista_kryteriów[0]
    ile_ofert = lista_kryteriów[1]
    
    for i in range(1,10000):
        url2 = url.replace("page=1",f"page={i}")
        driver.get(url2)

        poop_up(driver)
        driver.execute_script("window.scrollTo(0, 1000);")

        for i in driver.find_elements('xpath',"//a[@data-cy='listing-item-link']"):
            linki.append(i.get_attribute("href"))
            linki_unique=set(linki)

            if len(linki_unique) == ile_ofert:
                break

        if len(linki_unique) == ile_ofert:
            break
    
    driver.close()
    return(linki_unique)


    