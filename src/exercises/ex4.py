# Importem llibreries
import pandas as pd
import matplotlib.pyplot as plt

# Variables globals
from exercises.config import nom_alumne, date_time

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Definiu la funció FTR(data), que retorna el número de partits que han guanyat els locals, que han guanyat els
    visitants, o que han empatat (draw), en forma de dataframe (dataframe ftr).
    :param data: pd.DataFrame
    :return: pd.DataFrame
    '''

    # Contem el nombre de vegades que apareix H, V i D a la columna FTR, renombrem la columna i retornem el DataFrame
    nombre_partits = distr_gols_locals = data["FTR"].value_counts().to_frame()
    nombre_partits.columns = ["NombrePartits"]

    return nombre_partits

def plot_FTR(ftr: pd.DataFrame) -> None:
    '''
    Definiu la funció plot_FTR(ftr) que representa aquesta informació (eix x: H, A, D; eix y: nombre de partits)
    :param ftr: pd.DataFrame
    :return: None
    '''

    plt.figure(figsize=(8, 6))

    # Equips a la X i totals a la Y
    plt.bar(ftr.index,ftr['NombrePartits'])

    # Títos i noms dels eixos
    plt.xlabel('H (local), A (Visitant), D (Empat)')
    plt.ylabel('Total de partits')
    plt.title('Partits guanyants per local, visitant o empatatas')

    plt.savefig(f"img/grafica_ex4_{nom_alumne}_{date_time}.png")
