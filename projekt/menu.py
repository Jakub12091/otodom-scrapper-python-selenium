from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach', True)
import time


def poop_up(driver):
    try:
        element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(('xpath', '//button[@id="onetrust-accept-btn-handler"]')))
        element.click() 
    except:
        pass


def kryteria():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.otodom.pl/')

    poop_up(driver)

    #klik w wyszukiwarkę miejscowości
    element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable(('xpath', '//div[@data-cy="search.form.location.placeholder"]')))
    element.click()


#wybranie miejscowości do przeszukania
    while True:
        try:
            lokalizacja=str(input('Wpisz nazwę miejscowości, której mieszkania Cię interesują\n\
                                    \rJeżeli jest to popularna nazwa, wpisz miejscowość i powiat np. "Gniew tczewski" \n\
                                    \rMożesz też dopisać nazwę dzielnicy np. "Warszawa Bemowo"\n'))

            search_box=driver.find_element('xpath','/html/body/div[1]/main/section/div/form/div/div[1]/div[3]/div/div[1]/div/div[1]/input')
            search_box.clear()
            search_box.send_keys(lokalizacja)

            check_box = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(('xpath','//li[@data-testid="suggestions-item"]//label[@data-cy="checkboxButton"]')))
            check_box.click()

        except:
            print("Wystąpił problem z podaną lokalizacją. Czy podajesz prawidłową wartość? Spróbuj ponownie\n")
        else:
            print('wyszukam oferty dla:', driver.find_element('xpath','//li[@data-testid="suggestions-item"]').text)
            break
    
#wciśnij "szukaj"
    element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(('xpath', '//button[@data-cy="search.submit-form.default"]')))
    time.sleep(3) #wydaje się, że strona czasem potrzebuje jeszcze chwili przed klikiem, inaczej może załadować ogłoszenia dla całej polski
    element.click()
    
    time.sleep(8) #just in case, bo przechodzimy do nowej strony
    oferty1=(driver.current_url)

#wybór rynku
    while True:
        try:
            rynek = str(input('Interesują Cię mieszkania z rynku a) wtórnego b) pierwotnego c) oba?\nWpisz "a" lub "b" lub "c" by wybrać '))
        except:
            print('wystąpił błąd, czy na pewno wpisujesz "a", "b" lub "c"? Spróbuj ponownie\n')
        else:
            if rynek == "a":
                oferty2=oferty1.replace("market=ALL","market=SECONDARY")+'&page=1&limit=36'
                driver.get(oferty2)
                break
            elif rynek == "b":
                oferty2=oferty1.replace("market=ALL","market=PRIMARY")+'&page=1&limit=36'
                driver.get(oferty2)
                break
            elif rynek == "c":
                oferty2=oferty1+'&page=1&limit=36'
                break
            else:
                print('wystąpił błąd, czy na pewno wpisujesz "a", "b" lub "c"? Spróbuj ponownie/n')


    max_ofert = int(driver.find_element('xpath','//strong[@data-cy="search.listing-panel.label.ads-number"]//span[@class="css-19fwpg e1av28t50"]').text)

    while True:
        try:
            ile_ofert=int(input(f'Jaka liczba ofert Cię interesuje? Max. to {max_ofert} '))
        except:
            print("czy podałeś prawidłową wartość? Spróbuj ponownie\n")
        else:
            if ile_ofert <= max_ofert and ile_ofert > 0:
                break
            else:
                print('czy podałeś prawidłową wartość? Spróbuj ponownie\n')

    lista_return=[oferty2, ile_ofert]
    driver.close()
    return lista_return

