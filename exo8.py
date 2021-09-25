'''
*** EXO 8: Health Check ***
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond
à raison d'une requête toutes les n secondes (pas d'écrasement)

la périodicité sera fournie en entrée par l'utilisateur

On produira en sortie un fichier de log "health.log" qui contiendra:
- la date de la requete
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse
'''
print("*** EXO 8: Health Check ***")

# votre code ici

import requests, time, os
from datetime import datetime

websites=[
    {"name": "w3school", "url": "https://www.w3schools.com/"},
    {"name": "Github", "url":"https://github.crom/"},
    {"name": "Pypi", "url":"https://pypi.org/"},
    {"name": "Corriere", "url":"https://www.corriere.it/"},
    {"name": "truc.machin", "url":"http://www.truc.machin"},
    {"name": "Pypi forzajuve", "url":"https://pypi.org/project/forzajuve/"},
    {"name": "Tutorialsteacher", "url":"https://www.tutorialsteacher.com/python"}
]

delay=int(input("Délai entre chaque requête (en secondes): "))
number_times=int(input("Nombre de fois: "))

#Crée un dossier "logs" s'il n'existe pas déjà où les fichiers log seront mis
if not os.path.exists("logs"):
    os.makedirs("logs")

for i in range(number_times):

    for w in websites:
        
        filepath = "logs/"+w["name"].lower()+"_health.log"   

        try:
            print("------------")
            date=datetime.now()
            url_adress=w["url"]
            r = requests.get(w["url"],timeout=3)
            status_url=r.status_code
        
            print(datetime.now(),"   ",w["url"],"   ","Status Code:", status_url)
            
        except:
            print(datetime.now(),"   ",w["url"],"   ","Status Code:", status_url)
            
        with open(filepath, "a") as logFile :
            logFile.write(f"{date}   {url_adress}   Status Code: {status_url}\n")
            
    time.sleep(delay)  




