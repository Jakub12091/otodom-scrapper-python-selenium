import pandas as pd
pd.options.display.max_columns = 20
import time


def clean(df):
    print('Rozpoczynam czyszczenie...')
    time.sleep(1)

    #Cena
    df.Cena = df.Cena.apply(lambda x: x.replace("zł","").replace(" ","") if isinstance(x, str) else pd.NA)
    df.Cena = df.Cena.astype('Int64')

    #Cena_za_metr
    df.Cena_za_metr = df.Cena_za_metr.apply(lambda x: x.replace("zł/m²","").replace(" ","") if isinstance(x, str) else pd.NA)
    df.Cena_za_metr = df.Cena_za_metr.astype('Int64')

    #Powierzchnia
    df.Powierzchnia = df.Powierzchnia.apply(lambda x: x.replace("m²","").replace(" ","").replace(",",".") if isinstance(x, str) else pd.NA)
    df.Powierzchnia = df.Powierzchnia.astype('Float64')

    #Liczba_pokoi
    df.Liczba_pokoi = df.Liczba_pokoi.astype('Int64')

    #Piętro
    df[['Piętro','Piętra_w_budynku']] = df.Piętro.str.split('/',expand = True)
    
    df.Piętro = df.Piętro.apply(lambda x: '0' if isinstance(x,str) and x == 'parter' else ('-1' if isinstance(x,str) and x == 'suterana' else 
                                                                                           ('11' if isinstance(x,str) and '>' in x else x)))
    df.loc[df.Piętro == 'poddasze','Piętro'] = df.Piętra_w_budynku

    df.Piętro = df.Piętro.astype('Int64')
    df.Piętra_w_budynku = df.Piętra_w_budynku.astype('Int64')

    #Czynsz
    df.Czynsz = df.Czynsz.apply(lambda x: x.replace("zł", "").replace(" ","") if isinstance(x, str) else pd.NA)
    df.Czynsz = df.Czynsz.astype('Int64')

    #Balkon_ogród_taras
    df['Balkon'] = df.Balkon_ogród_taras.apply(lambda x: 1 if isinstance(x, str) and 'balkon' in x else (0 if isinstance(x, str) else pd.NA))
    df.Balkon = df.Balkon.astype('Int64')

    df['Ogródek'] = df.Balkon_ogród_taras.apply(lambda x: 1 if isinstance(x, str) and 'ogródek' in x else (0 if isinstance(x, str) else pd.NA))
    df.Ogródek = df.Ogródek.astype('Int64')

    df['Taras'] = df.Balkon_ogród_taras.apply(lambda x: 1 if isinstance(x, str) and 'taras' in x else (0 if isinstance(x, str) else pd.NA))
    df.Taras = df.Taras.astype('Int64')

    df.drop(columns = 'Balkon_ogród_taras', inplace = True)

    #object -> string
    for column in df:
        if df[column].dtype == 'O':
            df[column] = df[column].astype('string')
    


    df = df.loc[:, ['Tytuł','Cena','Cena_za_metr','Adres','Powierzchnia','Liczba_pokoi','Piętro', 'Piętra_w_budynku','Czynsz','Forma_własności',
                            'Stan_wykończenia','Balkon', 'Ogródek', 'Taras','Miejsce_parkingowe', 'Ogrzewanie',
                            'Rynek','Winda','Link']]   
    
    print(f'{df.info()}\nZrobione. Powyżej info o oczyszczonym zbiorze')
    time.sleep(3)
    return(df)


