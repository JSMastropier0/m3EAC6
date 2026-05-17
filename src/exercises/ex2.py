# Importem llibreries
import pandas as pd
import matplotlib.pyplot as plt

# Variables globals
from exercises.config import nom_alumne, date_time

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    '''
    definiu la funció total_matches(data), que retorna un dataframe matches_team_total amb els partits jugats per
    cada equip durant tots els anys.
    :param data: pd.DataFrame
    :return: pd.DataFrame
    '''

    # Creem dos sets amb els partits a casa i fora per cada equip contant les vegades que apareix cada equip en cada columna
    partits_casa = data["HomeTeam"].value_counts()
    partits_fora = data["AwayTeam"].value_counts()

    # Sumem els sets per tenir el total de partits jugats
    partits_total = partits_casa + partits_fora

    # Convertim el Set en DataFrame i li diem amb reset_index() que converteixi l'index del Set en columna (els equips)
    # Després renombrem les columnes del DataFrame i ho retornem
    equip_partits = partits_total.to_frame().reset_index()
    equip_partits.columns = ["Equip", "PartitsJugats"]

    return equip_partits

def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    '''
    definiu la funció plot_matches_team_total(matches_team_total), que representa aquesta informació (eix x: equips; eix y: número de partits total). Executeu la funció.
    :param matches_team_total: pd.DataFrame Les dades de partits per equip
    :return: None Crearà una gràfica a la carpeta /img
    '''

    # Creem el gràfic de barres, molt més ample que alt
    plt.figure(figsize=(15, 6))

    # Equips a la X i totals a la Y
    plt.bar(matches_team_total['Equip'], matches_team_total['PartitsJugats'])

    # Títos i noms dels eixos
    plt.xlabel('Equip')
    plt.ylabel('Total de partits')
    plt.title('Partits totals per equip')

    # Girem els noms a X perque siguin llegibles (matplotlib.org)
    plt.xticks(rotation=90)

    plt.savefig(f"img/grafica_ex2_{nom_alumne}_{date_time}.png")
