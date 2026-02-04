from django.shortcuts import render


def index(request):

    template = 'web/index.html'
    return render(request, template)
