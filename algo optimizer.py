import csv
from collections import namedtuple

with open('dataset2_Python+P7(1).csv', mode='r') as fichiercsv:
    reader = csv.reader(fichiercsv)
    next(reader)
    dictionnaire = {rows[0]: [int(float(rows[1])*100), float(rows[2])] for rows in reader if float(rows[1])*100 > 0}


portefeuille = 500 * 100


def calcule_benef(prix, benef_a_2_an):
    return prix * benef_a_2_an / 100


for key, value in dictionnaire.items():
    value.append(calcule_benef(value[0], value[1]))

sorted_dictionaire = sorted(dictionnaire, key=lambda ele: (dictionnaire[ele][2]))

Action = namedtuple("Action", "nom,prix,valeur")

liste = []

for action in sorted_dictionaire:
    liste.append(Action(action, dictionnaire[action][0], dictionnaire[action][2]))

tableau = []

for t in range(len(liste)+1):
    temp = []
    for index in range(portefeuille):
        temp.append(0)
    tableau.append(temp)

for t in range(1, len(liste)+1):
    for index in range(portefeuille):
        tableau[t][index] = tableau[t - 1][index]
        action_consideree = liste[t-1]
        valeur_total = tableau[t-1][index - action_consideree.prix] + action_consideree.valeur
        if index >= action_consideree.prix and tableau[t][index] < valeur_total and action_consideree.prix > 0:
            tableau[t][index] = valeur_total


def fonction(tableau):
    i = len(sorted_dictionaire)
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
        benef += element.valeur / 100
    print(f'les action à acheter sont :{action}')
    print(f'pour un cout total de :{cout_total}')
    print(f'le benefice total sera de :{benef} roupies ')


action_a_acheter = fonction(tableau)
