# Importem llibreries
import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
    '''
    definiu la funció add_points(data), que afegeix al dataset els punts aconseguits com a local i com a visitant,
    per cada partit. És a dir, creeu les columnes points_home i points_away, que poden agafar el valor de 3, 1 o 0.
    :param data: pd.DataFrame
    :return: pd.DataFrame
    '''

    # Creem les columnes sol.licitades mapejant els valors H, A i D a 3, 0 i 1 o 0,3,1 per local i visitant (pandas.pydata.org)
    data['points_home'] = data["FTR"].map({'H': 3, 'A': 0, 'D': 1})
    data['points_away'] = data["FTR"].map({'H': 0, 'A': 3, 'D': 1})

    return data

def fun_total_points(data: pd.DataFrame) -> pd.DataFrame:
    '''
    efiniu la funció fun_total_points(data), que calcula el total de punts aconseguits i acumulats des de 1995 per cada equip.
    Retorneu per cada equip el número de punts totals, en forma de tupla: variable Series i variable Dataframe
    (el Series i el Dataframe de fet contenen la mateixa informació). (És una proposta, un alumne pot decidir que només
    retorni la Series o el Dataframe).
    :param data: pd.DataFrame
    :return: pd.DataFrame He decidit, per ser coherent amb exercicis previs tornar un dataframe
    '''

    # Crearem dos series, pels punts a casa i els gols fora i després ho sumarem i convertirem a dataFrame
    punts_casa = data.groupby('HomeTeam')['points_home'].sum()
    punts_fora = data.groupby('AwayTeam')['points_away'].sum()
    punts_totals = (punts_casa + punts_fora).to_frame()
    punts_totals.columns = ['Punts_Totals']
    return punts_totals

def guanyador_historic(df_total_points: pd.DataFrame) -> str:
    '''
    efiniu la funció guanyador_historic(df_total_points), que retorna el guanyador d'aquesta lliga històrica i acumulada
    (l'equip que ha acumulat més punts). Executeu la funció i mostreu el guanyador històric.
    :param df_total_points: pd.DataFrame
    :return: str
    '''

    guanyador = df_total_points['Punts_Totals'].idxmax()
    return guanyador
