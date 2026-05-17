# Importem llibreries
import pandas as pd
import matplotlib.pyplot as plt

# Variables globals
from exercises.config import nom_alumne, date_time

def load_and_eda( file: str ) -> None:
    '''
    Definiu la funció load_and_eda(file), que carrega el dataset i elimina les columnes "HTHG", "HTAG", "HTR".
    La funció també mostra els primers i últims valors del dataset, i la informació més rellevant.
    :rtype: None
    :param file:str (path del fitxer a tractar)
    :return: pd.DataFrame (dataframe de pandas un cop net)
    '''

    # Carrego el fitxera a un dataFrame
    data = pd.read_csv(file)

    # I eliminem les columnes indicades amb inplace a True pq executi l'ordre
    data.drop( data[["HTHG", "HTAG", "HTR"]], axis=1, inplace=True)

    # Info del dataset, primers i últims valors
    print ("Infomració del dataset\n")
    print (data.info())
    print ("\n\n Primers valors del dataset\n")
    print (data.head())
    print ("\n\n Últims valors del dataset\n")
    print (data.tail())
    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    '''
    Definiu la funció plot_home_away_goals(data), que conté una figura amb dos plots. En la gràfica es mostra com és la
    distribució de gols marcats pels equips de casa i pels equips de fora. Ajuda: podeu utilitzar plt.boxplot
    :param data: pd.DataFrame
    :return: None
    '''

    # Creem el gràfic
    plt.figure(figsize=(8, 6))

    gols_casa = data['FTHG']
    gols_fora = data['FTAG']

    # Crear els boxplots
    plt.boxplot([gols_casa, gols_fora],
                labels=['Casa', 'Fora'])

    # Afegir títol i etiquetes
    plt.title('Distribució de gols marcats')
    plt.ylabel('Nombre de gols')

    # Printar la gràfica a un arxiu
    plt.savefig(f"img/grafica_ex1_{nom_alumne}_{date_time}.png")
