from itertools import combinations, chain
import csv
import time


start = time.time()


with open('dataset0_Python+p7.csv', mode='r') as fichiercsv:
    reader = csv.reader(fichiercsv)
    next(reader)
    dictionnaire = {rows[0]: [float(rows[1]), float(rows[2])] for rows in reader if float(rows[1])*100 > 0}

liste_actions = []
combinaison = []


for key in dictionnaire:
    liste_actions.append(key)

for i in range(len(liste_actions)):
    resulta = combinations(liste_actions, i+1)
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
                benefice_total = prix*benefice/100
                prix_total += prix
                benef += benefice_total
        if not prix_total > 500:
            possible_combinaison.append([test, benef, prix_total])
    meilleur_combinaison = sorted(possible_combinaison, key=lambda x: x[1], reverse=True)
    meilleur = meilleur_combinaison[0]
    print("la meilleur combinaison d'action est la suivante :")
    for action in meilleur[0]:
        print(f"l'{action}")
    print(f"pour un benefice total de : {meilleur[1]} roupie")
    print(f"pour une dépensse total de : {meilleur[2]} roupie")
    print(f" le temps d'exécussion est de : {time.time() - start} seconde")


combinaison_resultat()
