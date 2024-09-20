EXO 1

Création compte GROQ + génération TOKEN :

![Capture d’écran 2024-09-20 162338](https://github.com/user-attachments/assets/34ad9de1-d1c1-4426-bc33-cde8eebb40dd)


Création fichier .env avec mon TOKEN dedans puis rajout du .env dans le .gitignore pour que GITHUB ne récup pas.

Modification du fichier mini_groq.py pour le .env et importer os

L'application démarre 
![image](https://github.com/user-attachments/assets/8fb242ad-fdae-4442-baa4-8612dbaa3da8)


Exo 2 : Set up and Dockerize the FastAPI Application

Création d'un dossier "app" et rangement du fichier .py dedans.

Création d'un Dockerfile et rajout de uvicorn dans les requirements. image image

Build de l'image avec mes différentes paramètres :

image

lancement de mon conteneur via l'image créé précédemment :

image

Conteneur Docker fonctionnel, FastAPI lancé :

image

Ping du conteneur :

image

Création du script test.sh

image

Mise en fonctionnement du script pendant que le conteneur FASTAPI est en route :

image

exercice 3 : Create a development Branch and Implement testing

Question 1 :

Création de la branche dev :

image

Question 2 : création du fichier test_app.py pour tester mon fastapi:

image

Résultat du pytest :

image
