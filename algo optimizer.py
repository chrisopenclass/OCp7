import csv
from collections import namedtuple
import time


start = time.time()

with open('dataset1_Python+p7.csv', mode='r') as fichiercsv:
    reader = csv.reader(fichiercsv)
    next(reader)
    dictionnaire = {rows[0]: [int(float(rows[1])*100), float(rows[2]),
                    float(rows[1]) * float(rows[2])/100]
                    for rows in reader if float(rows[1])*100 > 0}


portefeuille = 500 * 100


Action = namedtuple("Action", "nom,prix,valeur")

liste = []

for action in dictionnaire:
    liste.append(Action(action, dictionnaire[action][0], dictionnaire[action][2]))


tableau = [[0 for x in range(portefeuille + 1)]for x in range(len(liste) + 1)]

print(f" le temps d'exécussion est de : {time.time() - start} seconde")
for t in range(1, len(liste)+1):
    for index in range(portefeuille):
        tableau[t][index] = tableau[t - 1][index]
        action_consideree = liste[t-1]
        valeur_total = tableau[t-1][index - action_consideree.prix] + action_consideree.valeur
        if index >= action_consideree.prix and tableau[t][index] < valeur_total:
            tableau[t][index] = valeur_total


def fonction(tableau):
    i = len(dictionnaire)
    p = portefeuille - 1
    liste_a_acheter = []
    action = []
    cout_total = 0
    benef = 0
    while i > 0:
        actual = tableau[i][p]
        if actual == tableau[i-1][p]:
            i -= 1
        else:
            liste_a_acheter.append(liste[i-1])
            p -= liste[i-1].prix
            i -= 1
    for element in liste_a_acheter:
        action.append(element.nom)
        cout_total += element.prix / 100
        benef += element.valeur
    print(f'les action à acheter sont :{action}')
    print(f'pour un cout total de :{cout_total}')
    print(f'le benefice total sera de :{benef} roupies ')


action_a_acheter = fonction(tableau)

print(f" le temps d'exécussion est de : {time.time() - start} seconde")
