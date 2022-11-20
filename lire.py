import csv

with open("information.csv") as fichier_csv:
    lire = csv.reader(fichier_csv, delimiter=',')
    for ligne in lire :
        print(ligne)