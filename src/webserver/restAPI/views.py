from django.http import HttpResponse


def home(request,fichier,json):
    with open(fichier, "w") as fichier:
            fichier.write(json)
    return HttpResponse(json)

