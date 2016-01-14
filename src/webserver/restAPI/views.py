
from __future__ import unicode_literals
from django.http import HttpResponse
from daemon.initialisation import *


def home(request,fichier,json):
    with open(fichier, "w") as fichier:
            fichier.write(json)
    return HttpResponse(json)

