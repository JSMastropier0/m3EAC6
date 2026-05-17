# Importem les llibreries necessàries
import pickle
import pandas as pd


#importem les nostres llibreries
# Les variables globals
from exercises.config import nom_alumne, date_time, autoria

# Els exercicis
from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches,plot_matches_team_total
from exercises.ex3 import goal_distribution, plot_goal_ditribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, fun_total_points, guanyador_historic
from exercises.ex6 import fun_total_goals, fun_total_goals_by_team, fun_resum_1996_2025, add_stadium_capacity
from exercises.ex7 import model_clusters, assignacio_clusters, plot_clusters


# Exercici 1

autoria (nom= nom_alumne, data= date_time, exercici= 1)
df = load_and_eda(file= "data/LaLiga_Matches.csv")
plot_home_away_goals(data= df)


# Exercici 2
autoria (nom= nom_alumne, data= date_time, exercici= 2)
# Executem la funció total_matches i mostrem els 10 primers valors del dataframe que retorna

partits_equip = total_matches(data= df)
print ("\n\nPrimers 10 equips:")
print (partits_equip.head(10))

# Executem plot_matches_team_total pq crei el gràfic a img

plot_matches_team_total(matches_team_total= partits_equip)

# Exercici 3

autoria (nom= nom_alumne, data= date_time, exercici= 3)

# Executeu la funció i mostreu el dataframe resultant

distr_gols_locals, distr_gols_visitants = goal_distribution(data=df)

print("\nQuantitat de partits per gols marcats pel local")
print (distr_gols_locals)
print("\nQuantitat de partits per gols marcats pel Visitant")
print (distr_gols_visitants)

# Cridem a plot_goal_ditribution perque crei la imatge

plot_goal_ditribution(distr_gols_locals=distr_gols_locals, distr_gols_visitants=distr_gols_visitants)


# Exercici 4

autoria (nom= nom_alumne, data= date_time, exercici= 4)

# Executeu la funció i mostreu el dataframe resultant

mombre_partits = FTR(data=df)

print("\nNombre de partits guanyats per Local (H) Visitant (A) i empatats (D)")
print (mombre_partits)

# Cridem a plot_FTR() perque crei la imatge a /img

plot_FTR(ftr=mombre_partits)


# Exercici 5

autoria (nom= nom_alumne, data= date_time, exercici= 5)

# Executeu la funció add_points i mostreu els 10 primers valors.

df_points = add_points(data=df)
print ("\nData original amb punts per partit afegits (10 línies)")
print (df_points.head(10))

# executeu la funció fun_total_points i mostreu els 10 primers valors.

punts_totals = fun_total_points(data=df_points)
print ("\nPunts totals per equip")
print (punts_totals.head(10))

# Mostrem el guanyador històric amb la funció guanyador_historic

print (f"\nEl guanyador històric de la sèrie (equip amb més punts) és: {guanyador_historic(df_total_points=punts_totals)}")


# Exercici 6

autoria (nom= nom_alumne, data= date_time, exercici= 6)

# Definiu la funció fun_total_goals(data), que retorna una tupla de tres números enters: (home_goals, away_goals, total_goals).
# Mostreu aquesta informació per pantalla

total_gols = fun_total_goals(data = df)
print(f"\nGols totals marcats com a Locl, Visitant i suma dels dos: {total_gols[0]}, {total_gols[1]}, {total_gols[2]}")

# Definiu la funció fun_total_goals_by_team(data), que retorna una tupla de tres dataframes:
# home_goals_by_team, away_goals_by_team, total_goals_by_team.
# Mostreu els 10 primers valors de total_goals_by_team.

gols_totals_per_equip = fun_total_goals_by_team(data = df)
print("\nPrimers 10 valors de total_goals_by_team:")
print (gols_totals_per_equip[2].head(10))

# Executeu la funció fun_resum_1996_2025( , , , ) i mostreu els primers valors del dataframe resum_1996_2025

resum_1996_2025 = fun_resum_1996_2025(total_points=punts_totals, home_goals=gols_totals_per_equip[0], away_goals=gols_totals_per_equip[1], total_goals=gols_totals_per_equip[2])
print("\nPrimeres línies de resum_1996:2005")
print(resum_1996_2025.head())

# Definiu la funció add_stadium_capacity(resum_1996_2025, stadium_capacity), que té per objectiu afegir al dataframe resum_1996_2025
# la informació de la capacitat dels estadis. Per tant, retorna el dataframe resum_1996_2025 amb una nova columna

stadium_capacity = {
    'Alaves': 19840,
    'Albacete': 17524,
    'Almeria': 18331,
    'Ath Bilbao': 53331,
    'Ath Madrid': 68456,
    'Barcelona': 99354,
    'Betis': 60270,
    'Cadiz': 21094,
    'Celta': 29000,
    'Compostela': 16666,
    'Cordoba': 20989,
    'Eibar': 8164,
    'Elche': 36017,
    'Espanol': 40500,
    'Extremadura': 11580,
    'Getafe': 17393,
    'Gimnastic': 14600,
    'Girona': 11810,
    'Granada': 19336,
    'Hercules': 29500,
    'Huesca': 9100,
    'La Coruna': 32490,
    'Las Palmas': 32400,
    'Leganes': 12454,
    'Levante': 26354,
    'Logrones': 16000,
    'Malaga': 30044,
    'Mallorca': 23142,
    'Merida': 14600,
    'Murcia': 31179,
    'Numancia': 8261,
    'Osasuna': 23576,
    'Oviedo': 30500,
    'Real Madrid': 81044,
    'Recreativo': 21670,
    'Salamanca': 17341,
    'Santander': 22222,
    'Sevilla': 43883,
    'Sociedad': 39500,
    'Sp Gijon': 29029,
    'Tenerife': 22824,
    'Valencia': 48600,
    'Valladolid': 27618,
    'Vallecano': 14505,
    'Villareal': 22500,
    'Villarreal': 22500,
    'Xerez': 20523,
    'Zaragoza': 20000
}

# Executeu la funció add_stadium_capacity i mostreu els primers valors de resum_1996_2025

resum_1996_2025 = add_stadium_capacity(resum_1996_2025=resum_1996_2025, stadium_capacity=stadium_capacity)
print("\nPrimeres línies de resum_1996:2005")
print(resum_1996_2025.head())


# Exercici 7

autoria (nom= nom_alumne, data= date_time, exercici= 7)

# Executeu el model amb 3 clústers. Mostreu els labels que heu obtingut (assignació dels equips a un dels clústers)

model_3 = model_clusters(df = resum_1996_2025, num_clusters = 3)
print("\nLabels obtinguts al model")
print(model_3.labels_)

# Definiu la funció assignacio_clusters(df, kmeans), que afegeix al dataset una nova columna amb els clústers assignats.
# Executeu la funció assignacio_clusters(df, kmeans) i mostreu els primers valors.
resum_1996_2025_3 = assignacio_clusters(df = resum_1996_2025, kmeans = model_3)
print("\nPrimers valors de resum_1996_2025 amb el cluster assignat (3 clustes):")
print(resum_1996_2025_3.head())

# Cridem a plot_clusters amb el model de 3 cluster pq crei la gràfica com a imatge a /img
# Executeu la funció plot_clusters(resum_1996_2025, 'total_goals', 'points')
plot_clusters(df=resum_1996_2025_3, attr1='TotalGols', attr2='PuntsTotals')

# Executeu la funció plot_clusters(resum_1996_2025, 'stadium_capacity', 'points')
plot_clusters(df=resum_1996_2025_3, attr1='CapacitatEstadi', attr2='PuntsTotals')

# Executeu el model amb 4 clústers. Mostreu els labels que heu obtingut (assignació dels equips a un dels clústers)

model_4 = model_clusters(df = resum_1996_2025, num_clusters = 4)
print("\nLabels obtinguts al model")
print(model_4.labels_)

# Definiu la funció assignacio_clusters(df, kmeans), que afegeix al dataset una nova columna amb els clústers assignats.
# Executeu la funció assignacio_clusters(df, kmeans) i mostreu els primers valors.
resum_1996_2025_4 = assignacio_clusters(df = resum_1996_2025, kmeans = model_4)
print("\nPrimers valors de resum_1996_2025 amb el cluster assignat (3 clustes):")
print(resum_1996_2025_4.head())

# Cridem a plot_clusters amb el model de 3 cluster pq crei la gràfica com a imatge a /img
# Executeu la funció plot_clusters(resum_1996_2025, 'total_goals', 'points')
plot_clusters(df=resum_1996_2025_4, attr1='TotalGols', attr2='PuntsTotals')

# Executeu la funció plot_clusters(resum_1996_2025, 'stadium_capacity', 'points')
plot_clusters(df=resum_1996_2025_4, attr1='CapacitatEstadi', attr2='PuntsTotals')

# Responeu a les següents preguntes: amb 4 clústers, quants equips hi ha en el clúster dels millors? Quins són?
print(f"\nAl cluster dels millors (2, segons la gràfica) hi ha { (resum_1996_2025_3['cluster'] == 2).sum()} equips")
print("I aquests equips són:")
print(resum_1996_2025_4[resum_1996_2025_4['cluster'] == 2])


# Suposem que tenim el següent equip que ha participat en la Lliga: (renombro labels a les que he estat utilitzant)
data = {
    "team_name": ["Europa"],
    "PuntsTotals": [1150],
    "GolsCasa": [650],
    "GolsFora": [440],
    "TotalGols": [1090],
    "CapacitatEstadi": [28000]
}

# Assigneu el seu clúster, amb el model de 4 clústers. Heu de tenir en compte que heu d'escalar les dades tal com les
# heu escalat en l'entrenament, i que aquesta informació la teniu guardada en el model model_4.pkl.

# Carreguem el diccionari de disc i creem variables pel scaler i model per facilitat posterior
with open('./model/model_4.plk', 'rb') as handle:
    model_dict = pickle.load(handle)

scaler = model_dict['scaler']
model = model_dict['model']

# Dades a DataFrame

europa = pd.DataFrame(data)
europa.drop('team_name', axis=1, inplace=True)

# Escalem les dades
X = pd.DataFrame(scaler.transform(europa),index=europa.index,columns=europa.columns)

# I Asignem el clúster
cluster = model.predict(X)

print(f"\nL'Europa estaria en el cluster {cluster}")
