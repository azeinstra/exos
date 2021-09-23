'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins un caractère spécial (/;|%, etc.)
La longueur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 6: Générateur de mot de passe ***")

from random import *


Minus="azertyuiopqsdfghjklmwxcvbn"
Maj=""
for i in range(len(Minus)):
    Maj+=Minus[i].upper()
special="!@#$%^&*()[]{};:,./<>?\|`~-=_+"
numbers="0123456789"

list_pwd=[]
all=Minus+Maj+special+numbers

print("--------------------")
print("Minuscules:", Minus)
print("Majuscules:", Maj)
print("Chiffres:", numbers)
print("Caractères spéciaux:",special)
print("--------------------")

try:
    lengh = int(input("Longueur du mot de passe (minimum 4) ? "))
    while lengh < 4:
        lengh = int(input("Longueur du mot de passe (minimum 4) ? "))
except:
    print("Saisie invalide")

list_pwd.append(choice(Minus))
list_pwd.append(choice(Maj))
list_pwd.append(choice(numbers))
list_pwd.append(choice(special))

if lengh == 4:
    shuffle(list_pwd)
    pwd="".join(list_pwd)
    print("Votre mdp est: ", pwd)
else:
    for n in range(lengh-4):
        x=choice(all)
        list_pwd.append(x)
        shuffle(list_pwd)
        pwd="".join(list_pwd)
    print("Votre mdp est: ", pwd)
        

