from itertools import combinations, chain
import csv


with open('liste_action.csv', mode='r') as fichiercsv:
    reader = csv.reader(fichiercsv)
    next(reader)
    dictionnaire = {rows[0]: [float(rows[1]), float(rows[2])] for rows in reader if float(rows[1])*100 > 0}

portefeuille = 500

liste = []
combinaison = []


def calcule_benef(prix, benef_a_2_an):
    return prix * benef_a_2_an / 100


for key in dictionnaire:
    liste.append(key)

for i in range(len(liste)):
    resulta = combinations(liste, i+1)
    combinaison.append(resulta)


def combinaison_resultat():
    possible_combinaison = []
    for test in chain.from_iterable(combinaison):
        prix_total = 0
        benef = 0
        for key in test:
            prix = float(dictionnaire[key][0])
            if prix > 0:
                benefice = float(dictionnaire[key][1])
                benefice_total = calcule_benef(prix, benefice)
                prix_total += prix
                benef += benefice_total
        if not prix_total > portefeuille:
            possible_combinaison.append([test, benef, prix_total])
    meilleur_combinaison = sorted(possible_combinaison, key=lambda x: x[1], reverse=True)
    return meilleur_combinaison


def extraction_meilleur(meilleur_combinaison):
    meilleur = meilleur_combinaison[0]
    print("la meilleur combinaison d'action est la suivante :")
    for action in meilleur[0]:
        print(f"l'{action}")
    print(f"pour un benefice total de : {meilleur[1]} roupie")
    print(f"pour une dépensse total de : {meilleur[2]} roupie")


meilleur_combinaison = combinaison_resultat()

extraction_meilleur(meilleur_combinaison)
