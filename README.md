# otodom scrapper mieszkań (python, selenium, chromedriver)

Projekt powstał tylko w celach naukowych. 
Użytkownik w trakcie działania programu zostanie poproszony o wpisanie kilku parametrów do konsoli, takich jak przeszukiwana miejscowość. 

Opisy modułów:

-moduł menu: zawiera funckję kryteria(), która przeprowadza użytkownika przez stronę główną, wybór miejscowości oraz rynku. Funkcja zwraca listę składającą się z 1) linka do ogłoszeń dotyczących danej miejscowości/rynku 2) liczby ofert do zescrapowania, podanej wcześniej przez użytkownika

-moduł scrapowanie_linków: jako argument pobiera listę zawierającą link do ogłoszeń oraz liczbę ofert do zescrapowania. Funckja zebranie_linków zapisze linki prowadzące bezpośrednio do ogłoszeń, zebrane zostaną tylko unikatowe linki, nie pojawią się duplikaty. Funkcja zwraca listę unikalnych linków do ogłoszeń

-moduł lista_funkcji: zawiera listę funkcji, które zostaną wykorzystane do zescrapowania danych bezpośrednio z ogłoszenia, takich jak m.in. adres, liczba pokoi

-main: wykorzystuje opisane wyżej moduły, by pozyskać listę linków z ogłoszeniami. Scraper wchodzi w każdy link, wykorzystuje listę_funkcji do zebrania danych w DataFrame (w przypadku braku danych wpisze "N/A"). Po wykonaniu scrapowania program zapyta o chęć zapisania wyników do xlsx
