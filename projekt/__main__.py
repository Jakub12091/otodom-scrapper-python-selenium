from menu import kryteria
from menu import poop_up
from scrapowanie_linków import zebranie_linków
import lista_funkcji as LF
from cleaner import clean

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
pd.options.display.max_columns = 16
pd.options.display.max_rows = 10
import numpy as np
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach', True)
import time


df = pd.DataFrame(columns=['Tytuł','Cena','Cena_za_metr','Adres','Powierzchnia','Liczba_pokoi','Piętro','Czynsz','Forma_własności',
                            'Stan_wykończenia','Balkon_ogród_taras', 'Miejsce_parkingowe', 'Ogrzewanie',
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
            dane = np.nan
        finally:
            nowy_rekord.append(dane)
    nowy_rekord.append(link)

    df.loc[len(df)] = nowy_rekord

driver.close()

while True:
    try:
        czyszczenie = str(input('Czy interesują Cię surowe dane ze strony? Mogę oczyścić dane poprzez m.in. zmianę dtypes \n\
                                \r(obecnie dtype niemal każdej kolumny to object). Wybrane kolumny zostaną rozbite na kilka kolumn. \n\
                                \rPełną informację o dokonywanych zmianach znajdziesz w pliku readme. Czy oszczyścić dane? (T/N)\n'))

        if czyszczenie == 'N':
            break
        elif czyszczenie == 'T':
            df = clean(df)
            break
        else:
            print('Czy podałeś prawidłową wartosć "T" lub "N"? Spróbuj ponownie \n')

    except Exception as e:
        print(f'{e}\nwystąpił problem. Czy podałeś prawidłową wartosć "T" lub "N"? Spróbuj ponownie \n')

print(df)
    
while True:
    try:
        zapis=str(input('Czy chcesz zapisać wyniki do xlsx? Jeżeli tak, wklej ścieżkę z nazwą_pliku.xlsx \n\
            \rJeżeli nie chcesz zapisywać wyników, wpisz "N", program zakończy działanie '))

        if zapis == "N":
            break
        else:
            df.to_excel(zapis, index = False, na_rep='NA')
            print('zapisano, kończę działanie... ')
            time.sleep(2)
            break
        
    except Exception as e:
        print(f'{e}\nwystąpił problem. Czy wpisujesz prawidłową ścieżkę zakończoną nazwą_pliku.xlsx? Spróbuj ponownie \n')

















