from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to DamiDrew, this is an application that predicts whether your team will win their next match")
