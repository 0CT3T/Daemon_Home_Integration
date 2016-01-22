from __future__ import unicode_literals
import sys
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from daemon.initialisation import *


@csrf_exempt
def home(request,fichier):
    if request.method == 'POST':
        print(request.body)
        with open(JSONdirectory + fichier, "w") as fichier:
            fichier.write(request.body.decode("utf-8") )
        return HttpResponse(status=201)

    return Http404("only POST methode")

