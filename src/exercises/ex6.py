# Importem llibreries
import pandas as pd



def fun_total_goals(data: pd.DataFrame ) -> tuple:
    '''
    Definiu la funció fun_total_goals(data), que retorna una tupla de tres números enters:
    (home_goals, away_goals, total_goals). Mostreu aquesta informació per pantalla.
    :param data: pd.DataFrame
    :return: tuple
    '''

    # Calculem els totals i els posem a la tupla, no els calculem a la tupla directament pq hauríem de fer el càlcul
    # dues vegades al fer el total.
    total_local = int((data['FTHG'].sum()))
    total_visitant = int((data['FTAG'].sum()))
    total_gols = (total_local, total_visitant, total_local + total_visitant)
    return total_gols


def fun_total_goals_by_team(data: pd.DataFrame) -> tuple:
    '''
    Definiu la funció fun_total_goals_by_team(data), que retorna una tupla de tres dataframes: home_goals_by_team,
    away_goals_by_team, total_goals_by_team
    :param data: pd.DataFrame
    :return: tuple Retornem una tupla amb 3 dataframes
    '''

    # Primer creem les series fent el sumatori, sumem per tenir la tercera i convertim tot a df dintre la tupla
    home_goals_by_team = data.groupby('HomeTeam')['FTHG'].sum()
    away_goals_by_team = data.groupby('AwayTeam')['FTAG'].sum()
    total_goals_by_team = home_goals_by_team + away_goals_by_team
    return (home_goals_by_team.to_frame(), away_goals_by_team.to_frame(), total_goals_by_team.to_frame())


def fun_resum_1996_2025(total_points:pd.DataFrame ,home_goals:pd.DataFrame ,away_goals:pd.DataFrame ,total_goals:pd.DataFrame ) -> tuple:
    '''
    Definiu la funció fun_resum_1996_2025( , , , ) que crea el dataframe resum_1996_2025 a partir de la concatenació dels
    4 dataframes que passeu com a arguments: total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team.
    :param total_points: pd.DataFrame
    :param home_goals: pd.DataFrame
    :param away_goals: pd.DataFrame
    :param total_goals: pd.DataFrame
    :return: pd.DataFrame
    '''

    resum_1996_2025 = pd.concat([total_points, home_goals, away_goals, total_goals], axis=1)
    resum_1996_2025.columns = ['PuntsTotals','GolsCasa','GolsFora','TotalGols']
    return resum_1996_2025


def add_stadium_capacity(resum_1996_2025: pd.DataFrame, stadium_capacity: dict)-> pd.DataFrame:
    '''
    Definiu la funció add_stadium_capacity(resum_1996_2025, stadium_capacity), que té per objectiu afegir al dataframe resum_1996_2025
    la informació de la capacitat dels estadis. Per tant, retorna el dataframe resum_1996_2025 amb una nova columna.
    :param resum_1996_2025: pd.DataFrame
    :param stadium_capacity: dict
    :return: pd.DataFrame
    '''

    resum_1996_2025['CapacitatEstadi'] = resum_1996_2025.index.map(stadium_capacity)

    return resum_1996_2025
