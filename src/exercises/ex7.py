# Importem llibreries
import pickle
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn import preprocessing

# Variables globals
from exercises.config import nom_alumne, date_time


def model_clusters(df: pd.DataFrame, num_clusters: int)-> object:
    '''
    Definiu la funció model_clusters(df, num_clusters), que retorna el model ja entrenat.
    :param df: pd.Dataframe dataframe de entrada.
    :param num_clusters: int representant el numero de clusters.
    :return: object el model ja entrenat
    '''

    # Normalitzem dades
    scaler = preprocessing.StandardScaler().fit(df)

    X = pd.DataFrame(scaler.transform(df),index=df.index,columns=df.columns)

    # Definim el model i entrenem
    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)

    # Guardar el resultat del model a la carpeta model/ i amb el nom model_3.plk o o model_4.plk. El model contindrà un
    # diccionari amb el valor de la variable scaler, amb el valor de num_clusters, i amb el model de kmeans.
    model_dict = {'scaler': scaler, 'num_clusters': num_clusters, 'model': model}
    with open(f'./model/model_{num_clusters}.plk', 'wb') as handle:
        pickle.dump(model_dict, handle)

    return model


def assignacio_clusters(df:pd.DataFrame , kmeans:object)->pd.DataFrame:
    '''
    Definiu la funció assignacio_clusters(df, kmeans), que afegeix al dataset una nova columna amb els clústers assignats.
    :param df: pd.Dataframe dataframe de entrada.
    :param kmeans: object el model de kmeans
    :return: pd.Dataframe amb els cluster afegits com a columna nova
    '''
    nou=df.copy()
    nou['cluster']= kmeans.labels_

    return nou

def plot_clusters(df:pd.DataFrame ,attr1:str , attr2:str)->None:
    '''
    efiniu la funció plot_clusters(df, attr1, attr2), que grafica els valors del dataset, amb l'eix x l'atribut attr1,
    i en l'eix y l'atribut attr2. Per cada clúster heu de mostrar un color.
    :param df: pd.Dataframe dataframe de entrada.
    :param attr1: str
    :param attr2: str
    :return: None Crearà una imatge amb el gràfic a /img
    '''

    # Creem un mapa de colors
    colormap = plt.cm.get_cmap('tab10')

    # Attr1 la X i attr2 a la Y
    plt.figure(figsize=(8, 6))
    for cluster in df['cluster'].unique():
        plt.scatter(df[df['cluster'] == cluster][attr1],
                    df[df['cluster'] == cluster][attr2],
                    color=colormap(cluster), label=cluster)

    # Títos i noms dels eixos
    plt.xlabel(attr1)
    plt.ylabel(attr2)
    plt.title(f'{attr1} vs {attr2}')
    plt.legend()

    # Girem els noms a X perque siguin llegibles (matplotlib.org)
    plt.savefig(f"img/grafica_ex7_{attr1}-{attr2}-{df['cluster'].max()+1}_clusters_{nom_alumne}_{date_time}.png")
