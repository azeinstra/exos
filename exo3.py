'''
*** Exo 3 ***
Ecrire un programme python qui calculera et affichera pour chacun des prix le prix TTC.
Créer une fonction qui calculera le prix TTC du prix HT qu'on lui fournira en entrée.
'''
print("*** EXO 3 ***")

prices = [14,100,30,10,8] #Prix HT
vat = 20 #taux de TVA en pourcentage

def TTC(price, vat = 20):
    return price+price*vat/100

for i in prices:
    print(round(TTC(i, 7), 1))

