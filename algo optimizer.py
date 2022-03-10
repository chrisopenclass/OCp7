import csv
from collections import namedtuple
import time
import math

start = time.time()

with open('dataset2_python+p7(1).csv', mode='r') as fichiercsv:
    reader = csv.reader(fichiercsv)
    next(reader)
    dictionnaire = {rows[0]: [math.floor(float(rows[1])), float(rows[2]),
                    float(rows[1]) * float(rows[2])/100]
                    for rows in reader if math.floor(float(rows[1])) > 0}

print(len(dictionnaire))
portefeuille = 500


Action = namedtuple("Action", "nom,prix,valeur")

liste = []

for action in dictionnaire:
    liste.append(Action(action, dictionnaire[action][0], dictionnaire[action][2]))


tableau = [[0 for x in range(portefeuille + 1)]for x in range(len(liste) + 1)]


for t in range(1, len(liste)+1):
    for solde_actuel in range(portefeuille):
        tableau[t][solde_actuel] = tableau[t - 1][solde_actuel]
        action_consideree = liste[t-1]
        valeur_total = tableau[t-1][solde_actuel - action_consideree.prix] + action_consideree.valeur
        if solde_actuel >= action_consideree.prix and tableau[t][solde_actuel] < valeur_total:
            tableau[t][solde_actuel] = valeur_total


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
        cout_total += element.prix
        benef += element.valeur
    print(f'les action à acheter sont :{action}')
    print(f'pour un cout total de :{cout_total}')
    print(f'le benefice total sera de :{benef} roupies ')


action_a_acheter = fonction(tableau)

print(f" le temps d'exécussion est de : {time.time() - start} seconde")
