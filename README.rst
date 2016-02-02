****************************************
Object_Home_Integration : a new way to see IOT
****************************************

Ce projet a pour objectif d'être intégré dans un objet. Il possède un daemon permettant le controle des différents modules de l'objet avec l'execution des fonctions et le ontrole des regles.
Un webserver permettant de recevoir un fichier au format JSON pour chaque module et attribut. 
Et une API totalement configurable en python pour obtenir la liste de tous les modules et les initialiser automatiquement.

Ce projet est écrit en python 3 et utilise la puissance du framework Django.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

===
API
===



L'API va permettre d'accèder à tous les modules/fonctions/attribut de l'objet ou lié. 
Elle est située dans le dossier daemon car essentiel à celui-ci.
Elle se configure automatiquement et permet un ajout ultra rapide d'un nouveau module/fonction/regle dans notre objet à l'aide de fichier de configuration.
Elle permet aussi d'initialiser la liste de règle pour le daemon.

voici le diagramme de classe du logiciel:

.. image:: UML.png

-------------
Configuration
-------------

Il s'agit de l'initialisation des différents modules en chargeant le fichier module.json.
Il va créer une variable "lobjet" contenant un dictionnaire de toutes les classes.

------
Module
------

Ils correspondent aux classes des objets implémentant les fonctions de la classe abstraite Hardware.
Ceci va permettre leur utilisation de maniere générique.
Le module défini dans LED.py est abouti et peut correspondre à un exemple pour l'ajout d'un objet.
chacun possede une fonction run qui va permettre d'utiliser le driver en fonction du mode de l'objet.

Dans la classe abstraite Hardware, il existe une fonction run qui va verifier l'état des fonctions et les regles.

.. code-block:: python

    def run(self):
            if self.startfunc != "":
                self.execfunction(self.startfunc,self.funcattribut)
                #resetfunction
                self.setfunction("",{})
    
            #stop les regles si fonction active
            try:
                if not self.threading.isAlive():
                    for rule in self.regle.values():
                        rule.exec()
            except:
                for rule in self.regle.values():
                        rule.exec()


D'autres fonctions permettent de recuperer des specifications pour les attributs, les fonctions ou les regles d'un objet, tels que changer une valeur, recuperer un fichier JSON ou bien changer le nom.

--------
Routage
--------

chaque objet possede aussi une liste de routage, permettant de lié la communication entre les objets. Ainsi l'objet LED par exemple ne pourra communiquer avec l'objet PIR s'il ne le possede pas dans sa liste. Ce qui permet de securiser ou non des objets.
A ce jour les objets sont connectés entre eux donc on fait abstraction du reseau mais la vision serait de permettre de lié une addresse IPv6 pour envoyer des requetes et faire communiquer le serveur.

--------
Attribut
--------

Chaque objet possede des attributs qui correspondent à des états de l'objet. Ils associent un nom, une valeur non typé et un objet.
Par exemple chaque objet possede un attribut mode qui correspond au mode de l'objet. Puis on peut ajouter un timer ou bien un attribut opacité pour la led par exemple.
Ces attributs seront changés lors de l'execution de regles ou de fonction. Et peuvent être utilisé lors de l'execution de l'objet.
Un exemple d'utilisation est le Timer.py utilisé dans la fonction Allumer.py permettant d'allumer la LED puis l'eteindre un certain temps.

.. code-block:: python

    def loop(self):
        if (time.time() - self.starttime)  > self.object.getparamvalue("Time"):
                self.stop()

--------
Fonction
--------

Les fonctions, qui sont prioratisé par rapport à l'execution des regles, permet l'execution unique d'un script dans un autre thread.
elles hérite de la classe fonction qui permet la gestion de l'arret mais aussi de coder les fonctions de maniere plus simple avec trois methodes setup, loop et finish selon la vision des scipt arduino.
Une seul fonction ne peut être appelé à la fois afin d'éviter une gestion de conflit.

Ceci est fait de cette maniere :

.. code-block:: python

    def run(self):
        self.setup()
        while not self.stopthread.isSet():
            self.loop()
        self.finish()

dedans nous recuperons aussi notre objet ce qui permet de recuperer la liste de routage de l'objet et executer ou modifier les attributs des objets connectés.

--------
Regles
--------

Chaque objet possede aussi une liste de regle. Abstraite de la classe regle, elles possedent un boolean active qui va permettre de les utiliser ou non. Elles sont appelé en continu ce qui les differencies des fonctions appelés seulement une fois.
Des conflits peuvent arriver ce qu'il faudra resoudre par un systeme de priorité.

C'est la fonction test qui sera appelé pour permettre le changement d'état, comme ceci pour la regle Allumer.py qui permet de garder la lumiere allumer :

.. code-block:: python

    def test(self):
        if self.object.getparamvalue("Mode") == "ETEINTE":
            self.object.setparamvalue("Mode", "ALLUMER")

--------
Driver
--------

Chaque objet va posseder un driver specifique à lui-même qui va permettre de faire abstraction de la couche Hardware.
Par exemple le driver_LED.py permet sur raspberry d'allumer une LED en PWM, l'éteindre ou bien faire blinker à une certaine frequence et opacité.

L'objectif serait de realiser de vrais driver en C avec modprobe.

-----------
Intégration
-----------

Pour intégrer cette API dans un projet il suffit d'importer la librairie Initialisation :
 
.. code-block:: python

    from daemon.initialisation import *
    
Un code d'exemple est present à la racine des src sous le nom de testmain.py, afin de permettre de voir l'appel des fonctions.
    
-------
A faire
-------

* Verifier que les dossiers existent sinon les créer
* Communication avec objets externes
* Check update des fichiers 
* Systeme de priorité pour les regles afin d'éviter les conflits.

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
des fichiers de configuration permettant d'installer le logiciel dans Apache sont present dans le dossier systeme à la racine.

------
LANCER
------
Pour lancer le webserver il suffit de lancer la commande :
après avoir installé django et djangorestframework. 
ou bien créer un environnement virtuel les contenant.

.. code-block:: bash

    $python3 manage.py runserver
    
------
TESTER
------
Ceci va créer un fichier led.json contenant les données en JSON après -d

.. code-block:: bash

    $curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://127.0.0.1:8000/led.json
    
-------
A faire
-------

* Création du service avec systemed
