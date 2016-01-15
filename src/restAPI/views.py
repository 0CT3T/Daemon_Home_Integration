
from __future__ import unicode_literals
from django.http import HttpResponse
from daemon.initialisation import *


def home(request,fichier,json):
    obj = lobjet["LED"].getJSON()
    with open('daemon/Configuration/json/' + fichier, "w") as fichier:
            fichier.write(json)
    return HttpResponse(obj)

