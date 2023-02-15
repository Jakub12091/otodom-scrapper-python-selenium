def tytuł(driver):
    return driver.find_element('xpath','//h1[@data-cy="adPageAdTitle"]').text

def cena(driver):
    return driver.find_element('xpath','//strong[@aria-label="Cena"]').text

def cena_za_metr(driver):
    return driver.find_element('xpath','//div[@aria-label="Cena za metr kwadratowy"]').text

def adres(driver):
    return driver.find_element('xpath','//a[@aria-label="Adres"]').text

def powierzchnia(driver):
    return driver.find_element('xpath','//div[@aria-label="Powierzchnia"]//div[@class="css-1wi2w6s estckra5"]').text

def liczba_pokoi(driver):
    return driver.find_element('xpath','//div[@aria-label="Liczba pokoi"]//div[@class="css-1wi2w6s estckra5"]').text

def piętro(driver):
    return driver.find_element('xpath','//div[@aria-label="Piętro"]//div[@class="css-1wi2w6s estckra5"]').text

def czynsz(driver):
    return driver.find_element('xpath','//div[@aria-label="Czynsz"]//div[@class="css-1wi2w6s estckra5"]').text

def forma_własności(driver):
    return driver.find_element('xpath','//div[@aria-label="Forma własności"]//div[@class="css-1wi2w6s estckra5"]').text

def stan_wykończenia(driver):
    return driver.find_element('xpath','//div[@aria-label="Stan wykończenia"]//div[@class="css-1wi2w6s estckra5"]').text

def balkon_ogród_taras(driver):
    return driver.find_element('xpath','//div[@aria-label="Balkon / ogród / taras"]//div[@class="css-1wi2w6s estckra5"]').text

def miejsce_parkingowe(driver):
    return driver.find_element('xpath','//div[@aria-label="Miejsce parkingowe"]//div[@class="css-1wi2w6s estckra5"]').text

def ogrzewanie(driver):
    return driver.find_element('xpath','//div[@aria-label="Ogrzewanie"]//div[@class="css-1wi2w6s estckra5"]').text

def rynek(driver):
    return driver.find_element('xpath','//div[@aria-label="Rynek"]//div[@class="css-1wi2w6s estckra5"]').text

def winda(driver):
    return driver.find_element('xpath','//div[@aria-label="Winda"]//div[@class="css-1wi2w6s estckra5"]').text

funkcje=[tytuł, cena, cena_za_metr, adres, powierzchnia, liczba_pokoi, piętro, czynsz, forma_własności,
                stan_wykończenia, balkon_ogród_taras, miejsce_parkingowe, ogrzewanie, rynek, winda]

