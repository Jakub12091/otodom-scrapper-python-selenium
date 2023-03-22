# otodom scrapper ogłoszeń mieszkań na sprzedaż (python, selenium, chromedriver)

Projekt powstał tylko w celach naukowych. 
Użytkownik w trakcie działania programu zostanie poproszony o wpisanie kilku parametrów do konsoli, takich jak przeszukiwana miejscowość. 

Opis modułów:

-moduł menu: zawiera funckję 'kryteria', która przeprowadza użytkownika przez stronę główną, wybór miejscowości oraz rynku. Funkcja zwraca listę składającą się z 1) linka do wyników wyszukiwanie ogłoszeń dotyczących danej miejscowości/rynku 2) liczby ofert do zescrapowania, podanej wcześniej przez użytkownika

-moduł scrapowanie_linków: zawiera funkcję 'zebranie_linków', która jako argument pobiera listę składającą się z linka do wyników wyszukiwania oraz liczby ofert do zescrapowania (lista, którą zwróci opisana wyżej funkcja kryteria). 
Funckja 'zebranie_linków' zapisze linki prowadzące bezpośrednio do ogłoszeń, zebrane zostaną tylko unikatowe linki, nie pojawią się duplikaty. Funkcja zwraca listę unikalnych linków do ogłoszeń

-moduł lista_funkcji: zawiera listę funkcji, które zostaną wykorzystane do zescrapowania danych bezpośrednio z ogłoszenia, takich jak m.in. adres, liczba pokoi

-main: wykorzystuje opisane wyżej moduły, by pozyskać listę linków z ogłoszeniami. Scraper wchodzi w każdy link, wykorzystuje listę_funkcji do zebrania danych w DataFrame. Po wykonaniu scrapowania program zapyta o chęć oczyszczenia danych (moduł cleaner) oraz zapisania wyników do xlsx. 

-cleaner: zawiera funkcję 'clean', umożliwia oczyszczenie danych. W ramach czyszczenia zmienione zostaną dtypes na te odpowiadające roli zmiennej (przykładowo "Powierzchnia" z object na Float64), braki danych w DataFramie pojawią się w formie pd.NA.

Kolumna "Piętro", która często zawiera informację o piętrze oraz ilości pięter budynku (np. "2/9") zostanie rozbita na dwie kolumny, "Piętro"(2) oraz "Piętra_w_budynku"(9). Wartości "parter" zostaną zamienione na 0, suterana na -1. Piętra wyższe niż 10 są zapisywane w ogłoszeniach jako ">10" - im przypisana zostanie wartość 11, z jednym wyjątkiem - wartościom piętra "poddasze" zostanie przypisana wartość najwyższego piętra (kolumna "Piętra_w_budynku"). 

Kolumna "Balkon_ogród_taras" rozbita zostanie na trzy kolumny "Balkon", "Ogródek", "Taras". Wartości przechowywane przez te kolumny to 1 w przypadku występowania charakterystyki, 0 w przypadku jej braku, pd.NA w przypadku braku danych. 

Kolumny w DataFrame po oczyszczeniu:

![image](https://user-images.githubusercontent.com/115424802/227053843-cc32e835-5d43-401e-8bb3-9f4dc4ac6894.png)

W związku ze zmianą dtypes z rekordów znikną oznaczenia waluty czy powierzchni (zł, m²). Przykładowa baza po imporcie do xlsx przentuje się następująco:
![image](https://user-images.githubusercontent.com/115424802/227054867-d5f87533-c298-46ae-9060-659878b33ba8.png)


