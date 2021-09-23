'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

import csv

#Nom du film le mieux noté
with open("deniro.csv", "r") as csvFile :
    rows = csv.reader(csvFile, delimiter=",")
    next(rows) 

    sort_score=sorted(rows,key=lambda test: test[1], reverse=True)
    best_film_score=sort_score[0][2]
    print("Le film avec le meilleur score est:", best_film_score)

#Nombre de films entre 2000 et 2010
with open("deniro.csv", "r") as csvFile :
    rows = csv.reader(csvFile, delimiter=",")
    next(rows) 
    times=0
    for r in rows:
        year=int(r[0].strip().strip('"'))
        if year >2000 and year<2010:
            times+=1
    print(times,"films sont sortis entre 2000 et 2010")

#Fichier deniro-report.txt avec les résultats
with open("deniro-report.txt", "w") as txtFile :
    txtFile.write(f"Le titre ayant obtenu le meilleur score est {best_film_score}.\n{times} films sont sortis entre 2000 et 2010.")
