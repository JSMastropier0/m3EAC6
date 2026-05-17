from datetime import datetime

# Definim les variables solicitades
nom_alumne = "Rodrigo_Santos_Gallego"
date_time = datetime.now().strftime('%Y%m%d_%H%M%S')

# Funció on printem les variables per demostrar autoria
def autoria( nom: str, data: str, exercici: int) -> None:
    '''
    Farem servir aquesta funció per printar el nom de l'alumne, data d'execució i exercici en curs tal i com demana
    a l'enunciat, però posat més "bonico"
    :param nom: str
    :param data: str
    :param exercici: int
    :return: None  No retornem res, printem per pantalla el quadre
    '''
    print ("\n************************************************************")
    print ("*                                                          *")
    print("*"+" " * ((58 - len(nom_alumne)) // 2 + (58 - len(nom_alumne)) % 2 ) + nom_alumne + " " * ((58 - len(nom_alumne)) // 2) + "*")
    print("*" + " " * ((58 - len(date_time)) // 2 + (58 - len(date_time)) % 2 ) + date_time + " " * (
                (58 - len(date_time)) // 2) + "*")
    print(f"*                        Exercici {exercici}                        *")
    print("*                                                          *")
    print("************************************************************")
