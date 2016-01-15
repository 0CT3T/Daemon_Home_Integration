****************************************
Object_Home_Integration : a new way to see IOT
****************************************

Ce projet a pour rôle d'être integrer dans un objet. il possede un daemon permettant le controle des Modules de l'objet.
Un webserver permettant de recevoir un fichier au format JSON pour chaque module. 
Et une API totalement configurable en python pour obtanir la liste de tous les modules.

Ce projet est ecrit en python et utilise la puissance du framework Django.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

===
API
===

L'API va permettre d'acceder à tous les modules de l'objet. 
Elle est situé dans le dossier daemon car essentiel à celui-ci.
Elle se configure automatiquement et permet un ajout ultra rapide d'un nouveau module dans notre objet à l'aide de fichier de configuration.
Elle permet aussi d'initialiser la liste de regle pour le daemon.

-------------
Configuration
-------------

Il s'agit de l'initialisation des differents modules en chargeant le fichier module.json.
Il va aussi créer trois variables lobjet contenant un dictionnaire de toutes les classes, lmodule permettant de loader les classes et lrules pour la liste de regle.

------
Module
------

Ils correspondent aux classes des objets implementant les fonctions de la classe abstraite Hardware.
Ceci va permettre leur utilisation de maniere generique.
Un modele de Module fini est celui de LED.py.
Un exemple d'utilisation de tous les objets se trouve dans exemple.py

-----
Rules
-----

Ils correspondent aux classes de regle qui vont se vérifier en continu avec le daemon.
Un exemple d'une regle est ruleexemple.py

-----------
Integration
-----------

pour integrer cet API dans un projet il suffit d'importer la librairie Initialisation :
 
.. code-block:: python
    from daemon.initialisation import *
    
-------
A faire
-------

* Ajout des autres modules et regles
* fichier JSON specifique aux modules
* loader tous les fichiers dans le repertoire au lieu d'un fichier de configuration
* check update

======
DAEMON
======

Le daemon est un executable qui va en continue vérifier si une regles est valide et executer le code d'un objet en fonction de son etat chargé dans un fichier JSON associé.

------
LANCER
------
Pour executer le daemon il suffit de lancer la commande :

.. code-block:: bash
    python3 launchdaemon.py
    
-------
A faire
-------

* Creation du service avec systemd

=========
WEBSERVER
=========

Le webserver codé en python grace au framework django va recevoir une requete POST et créer le fichier recu dans l'url avec dedans les données contenu dans le body.
Ceci va permettre d'envoyer les nouvelles configuration d'un objet avec une requete HTTP.

------
LANCER
------
Pour lancer le webserver il suffit de lancer la commande :
apres avoir bien sûre installer django et djangorestframework. 
ou bien créer un environnement virtuel les contenant.

.. code-block:: bash
    python manage.py runserver
    
------
TESTER
------
Ceci va créer un fichier led.json contenant les donnée en json apres -d

.. code-block:: bash
    curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://127.0.0.1:8000/led.json
    
-------
A faire
-------

* Creation du service avec systemd
* Mise en place avec Apache
* Resoudre probleme de sécurité pour faille csv