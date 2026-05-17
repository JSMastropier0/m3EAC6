# m3EAC6 Rodrigo Santos Gallego

Aquest programari és el exercici EAC6 del módul M3 del curs d'especiacització en IA i Big Data de FP al IOC.

L'estructura del projecte és la següent:

>- src/
>    - main.py: Fitxer principal. Executa els diferents exercicis de l'EAC.
>    - exercises/: conté les funcions dels diferents exercisis.
>    - exercises/ex1.py, etc: Conté les funcions que definim en l'exercici 1, etc.
>    - ...
>    - data/: el dataset
>    - img/: imatges generades
>    - model/: models d’IA generats
>- tests/:
>    - tests_ex6_fun_total_goals.py: només se’t demanarà test sobre l’exercici 6
>- doc/: documentació generada
>- screenshots/: Captures de pantalla sollicitades
>- requirements.txt: llibreries necessàries
>- README.md: Aquest arxiu. Informació sobre el projecte, com executar-lo, com comprovar el linting, generar la documentació i executar els tests.
>- LICENSE: fitxer de llicència

## Requeriments

Per poder instal.lar les llibreris necessàries en un entorn venv net, haureu d'executar, dintre d'aquest entorn virtual, i des de l'arrel del projecte la següent línia

>pip install -r requirements.txt

Informació sobre entorns venv: https://docs.python.org/3/library/venv.html

## Execució

Per executar el projecte, entrarem en la carpeta /src i executarem main.py:

>\>cd /src
> 
>\>python3 main.py



## Ex 9. Linting

Per comprovar el linting, haurem d'accedir a la carpeta /pylint des de l'arrel del projecte i des d'allà executar el pylint:
> pylint ../src/exercises/ex7.py

on ../src/exercises/ex7.py és l'arxiu que volem testejar.

## Ex 10 Documentació

La documentació de les funcions està a la carpeta /doc dintre l'arrel del projecte.
Per generar-la, previament, s'ha da'haver creat els docstrings a les funcions, com per exemple:

>'''
>    Definiu la funció model_clusters(df, num_clusters), que retorna el model ja entrenat.
> 
>    :param df: pd.Dataframe dataframe de entrada.
> 
>    :param num_clusters: int representant el numero de clusters.
> 
>    :return: object el model ja entrenat
>    '''

Llavors cridem la funció gendocs.py des de l'arrel del projecte:

>python3 gendoc.py

## Ex 11 Tests

Per executar el test sobre la funció fun_total_goals del exercici 6, haurem de fer, des del directori arrel del projecte:

>python3 -m unittest discover

I ens ha de donar un resultat com aquest:

>rodrigo@EnterpriseE:~/PycharmProjects/EAC6_Rodrigo_Santos> python3 -m unittest discover
>
>---------------------------------------------------------------------
>ran 1 test in 0.001s
>
>OK


## git

Per pujar la comanda a github, farem servir les següents comandes des de l'arrel del projecte:
(És necesari tenir git instal.lat al host)

>git init
> 
>git add .
> 
>git commit -m "first commit"
> 
>git branch -M main
> 
>git remote add origin git@github.com:JSMastropier0/EAC6_Rodrigo_Santos.git
> 
>git push -u origin main
 
On haureu de substituïr JSMastropier0/EAC6_Rodrigo_Santos.git pel vostre usuari i el nom de projecte que li hagueu posat

Si és el primer cop que feu servir git o voleu fer servir un usuari diferent de l'habitual, haureu de fer, abans del commit:

>git config user.email rodrigo@r3afoto.org
> 
> git config user.name JSMastropier0

Evidentment, amb el vostre correu i usuari

## Llicéncia

Aquest programari es pot distribuïr sota llicéncia GPL3, amb els termes que podeu trobar a l'arxiu LICENSE