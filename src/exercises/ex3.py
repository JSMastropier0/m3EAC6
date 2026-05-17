# Importem llibreries
import pandas as pd
import matplotlib.pyplot as plt

# Variables globals
from exercises.config import nom_alumne, date_time

def  goal_distribution(data: pd.DataFrame) -> pd.DataFrame:
    '''
    definiu la funció goal_distribution(data), que retorna dos dataframes: distr_gols_locals, distr_gols_visitants.
    Aquests dataframes contenen com a índex el número de gols marcats (per ex, FTHG), i com a columna el número de
    partits que s'han marcat aquest número de gols. Per exemple, hi ha 2598 partits en que FTHG=0
    (els equips locals no van marcar cap gol).
    :param data: pd.DataFrame
    :return: pd.DataFrame retornarme 2 dataframes  distr_gols_locals, distr_gols_visitants
    '''

    # Comptem el nombre de vegades que apareix cada valor ho pasem a DataFrame i ordenem per index (pandas.pydata.org)
    distr_gols_locals = data["FTHG"].value_counts().to_frame().sort_index()
    distr_gols_visitats = data["FTAG"].value_counts().to_frame().sort_index()

    # Renombrem la columna a un valor més descritiu
    distr_gols_locals.columns = ["NombrePartits"]
    distr_gols_visitats.columns = ["NombrePartits"]

    return distr_gols_locals, distr_gols_visitats


def plot_goal_ditribution(distr_gols_locals: pd.DataFrame, distr_gols_visitants: pd.DataFrame)-> None:
    '''
    definiu la funció plot_goal_ditribution(distr_gols_locals, distr_gols_visitants) per representar aquesta informació
    (una gràfica, dos plots).
    :param distr_gols_locals: pd.DataFrame
    :param distr_gols_visitants: pd.DataFrame
    :return: None Crearà una imatge amb la gràfica a /img
    '''

    plt.figure(figsize=(8, 6))

    # Gràfica equips locals
    plt.subplot(1, 2, 1)  # 1 fila i 2 columnes, posicionat en la 1a columna
    plt.title("Gols equip local")
    plt.bar(distr_gols_locals.index, distr_gols_locals['NombrePartits'])

    # Gràfica equips visitants
    plt.subplot(1, 2, 2)  # 1 fila i 2 columnes, posicionat en la 1a columna
    plt.title("Gols equip Visitant")
    plt.bar(distr_gols_visitants.index, distr_gols_visitants['NombrePartits'])

    plt.savefig(f"img/grafica_ex3_{nom_alumne}_{date_time}.png")
