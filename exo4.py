'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

def number():
    num=int(input("Chiffre: "))
    return num

def sum_number(list):
    for i in list:
        n = sum(list)
    return n

x=number()
numberlist=[]

while x != 0:
    numberlist.append(x)
    print("Les  valeurs que vous avez déjà saisies: ", numberlist)
    print("La somme des valeurs saisies est: ", sum_number(numberlist))
    x=number()


      