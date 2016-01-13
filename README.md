# Daemon_Home_Integration

Ce projet a pour rôle d'être integrer dans le webserver Django sur la box, dans l'optique de fournir l'architecture des objets et créer automatiquement les fichiers JSON à envoyer.
Il se compose essentiellement en deux parties :

## Configuration

Il s'agit de l'initialisation des differents modules en chargeant le fichier module.json
et la creation de deux variables lobjet contenant toutes les classes et lmodule permettant de loader les classes.

## Module

Ils correspondent aux classes des objets implementant les fonctions de la classe abstraite Hardware permettant leur utilisation.
Un modele de Module fini est celui de LED.py
Un exemple d'utilisation de tous les objets se trouve dans exemple.py


A faire:

* Ajout des autres modules
* fichier JSON specifique aux modules
* loader tous les fichiers dans module au lieu d'un fichier
* Ajout des regles
* Ajout du Daemon
* check update
