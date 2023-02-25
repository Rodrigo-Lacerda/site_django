from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("case-sucesse/", views.case_sucesse, name="case-sucesse"),
    path("site-oficial/", views.site_oficial, name="site-oficial"),
]
