from django.shortcuts import render


# index page
def index(request):
    return render(request, 'templates/index.css')
