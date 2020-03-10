from django.urls import path
from . import views

app_name = "address"

urlpatterns = [
    path("", views.addressView, name="index"),
    path("<str:address>/", views.addressView, name="address")
]