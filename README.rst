****************************************
Object_Home_Integration : a new way to see IOT
****************************************

Ce projet a pour objectif d'être intégré dans un objet. Il possède un daemon permettant le controle des différents modules de l'objet.
Un webserver permettant de recevoir un fichier au format JSON pour chaque module. 
Et une API totalement configurable en python pour obtenir la liste de tous les modules.

Ce projet est écrit en python et utilise la puissance du framework Django.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

===
API
===

L'API va permettre d'accèder à tous les modules de l'objet. 
Elle est située dans le dossier daemon car essentiel à celui-ci.
Elle se configure automatiquement et permet un ajout ultra rapide d'un nouveau module dans notre objet à l'aide de fichier de configuration.
Elle permet aussi d'initialiser la liste de règle pour le daemon.

-------------
Configuration
-------------

Il s'agit de l'initialisation des différents modules en chargeant le fichier module.json.
Il va aussi créer trois variables: "lobjet" contenant un dictionnaire de toutes les classes, "lmodule" permettant de loader les classes et "lrules" pour la liste des règles.

------
Module
------

Ils correspondent aux classes des objets implémentant les fonctions de la classe abstraite Hardware.
Ceci va permettre leur utilisation de maniere générique.
Le module défini dans LED.py est abouti.
Un exemple d'utilisation de tous les objets se trouve dans exemple.py

-----
Rules
-----

Ils correspondent aux classes de règles qui vont être vérifiées de manière continue avec le daemon.
Un exemple de règle est ruleexemple.py

-----------
Intégration
-----------

Pour intégrer cette API dans un projet il suffit d'importer la librairie Initialisation :
 
.. code-block:: python

    from daemon.initialisation import *
    
-------
A faire
-------

* Ajout des autres modules et règles
* Fichier JSON spécifique aux modules
* Loader tous les fichiers dans le repertoire au lieu d'un fichier de configuration
* Check update

======
DAEMON
======

Le daemon est un exécutable qui va vérifier, de manière continue, que toutes les règles sont bien respectées, sinon il exécute le code d'un objet en fonction de son état chargé dans un fichier JSON associé.

------
LANCER
------
Pour exécuter le daemon il suffit de lancer la commande :

.. code-block:: bash

    $python3 launchdaemon.py
    
-------
A faire
-------

* Création du service avec systemd

=========
WEBSERVER
=========

Le webserver est codé en python via le framework Django et reçoit une requête POST, crée un fichier JSON qui passe dans l'url contenant des données.
Ceci va permettre d'envoyer les nouvelles configuration d'un objet avec une requete HTTP.

------
LANCER
------
Pour lancer le webserver il suffit de lancer la commande :
après avoir installé django et djangorestframework. 
ou bien créer un environnement virtuel les contenant.

.. code-block:: bash

    $python manage.py runserver
    
------
TESTER
------
Ceci va créer un fichier led.json contenant les données en JSON après -d

.. code-block:: bash

    $curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://127.0.0.1:8000/led.json
    
-------
A faire
-------

* Création du service avec système
* Mise en place avec Apache
* Résoudre problème de sécurité pour faille csv
