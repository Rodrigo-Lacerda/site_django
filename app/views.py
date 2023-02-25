from django.shortcuts import render

# Create your views here.
# index page
def index(request):
    return render(request, 'app/index.html')


# case sucesse
def case_sucesse(request):
    return render(request, "app/case-sucesse.html")


# site oficial of Django-project
def site_oficial(request):
    return render(request, "app/site-oficial.html")