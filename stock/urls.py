from django.urls import path

from . import views

app_name = "stock"

urlpatterns = [
    path("", views.storeListView, name="list"),
    path("get-data/", views.getDataView, name="get"),
    path("<str:store>/", views.storeDetailView, name="detail"),
]
