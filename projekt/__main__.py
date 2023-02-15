from menu import kryteria
from scrapowanie_linków import zebranie_linków
import lista_funkcji as LF
from menu import poop_up

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach', True)
import time



df = pd.DataFrame(columns=['Tytuł','Cena','Cena za metr2','Adres','Powierzchnia','Liczba pokoi','Piętro','Czynsz','Forma własności',
                            'Stan wykończenia','Balkon / ogród / taras', 'Miejsce parkingowe', 'Ogrzewanie',
                            'Rynek','Winda','Link'])

#link do strony z ogłoszeniami dla wybranej lokalizacji oraz liczba ogłoszeń, której potrzebuje użytkownik, moduł menu funkcja kryteria()
lista_kryteriów = kryteria()
#linki ogłoszeń bez duplikatów pozyskane z funkcji zebranie_linków z modułu scrapowanie_linków
linki_unique = zebranie_linków(lista_kryteriów)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


for link in linki_unique:
    nowy_rekord=[]
    driver.get(link)

    poop_up(driver)

    for funkcja in LF.funkcje:
        try:
            dane = funkcja(driver)
        except:
            dane = "N/A"
        finally:
            nowy_rekord.append(dane)
    nowy_rekord.append(link)

    df.loc[len(df)] = nowy_rekord

driver.close()

print(df)
    
while True:
    try:
        zapis=str(input('Czy chcesz zapisać wyniki do xlsx? Jeżeli tak, wklej ścieżkę z nazwą_pliku.xlsx \n\
            \rJeżeli nie chcesz zapisywać wyników, wpisz "N", program zakończy działanie'))

        if zapis == "N":
            break
        else:
            df.to_excel(zapis)
            print('zapisano, kończę działanie...')
            time.sleep(2)
            break
    except:
        print('wystąpił problem. Czy wpisujesz prawidłową ścieżkę zakończoną nazwą_pliku.xlsx? Spróbuj ponownie \n')

















