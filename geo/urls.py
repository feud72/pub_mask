from django.urls import path
from . import views

app_name = "geo"

urlpatterns = [
    path("", views.geoView, name="index"),
    path("<str:lat>/<str:lng>", views.geoView, name="geo"),
]
