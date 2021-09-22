'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

#Importation des modules OS et shutil
import os
import shutil

#Création du dossier FlagsBis
try:
    os.mkdir("FlagsBis")
    print ("Le dossier FlagsBis a été créé.")
except FileExistsError:
    print("Le dossier FlagsBis est déjà créé.")
except:
    print("Le dossier FlagsBis ne peut pas être créé.")


numMovFiles=0
files=os.listdir("./")

for f in files:

    extension = f[-3:]
    flag_list=[]

    if extension == "png" and f[0:] != "missing.png":
        #Ajout des images dans une liste
        flag_list.append(f[:2]+f[-4:])

        #Changement du nom des images
        for i in range(len(flag_list)):
            flag_list[i]=flag_list[i][:2].upper()+flag_list[i][2:]
            print("Le fichier",str(f).strip("[]"), "a été renommé en", str(flag_list).strip("[]"))
            #Déplacement des images dans le dossier "FlagsBis"
            os.replace("./" + f , "./FlagsBis/"+ flag_list[i])
            numMovFiles+=1
            print("Le fichier ",str(flag_list).strip("[]"), "a été déplacé dans le dossier FlagsBis.")

print("%d fichiers ont été déplacés" %numMovFiles)
