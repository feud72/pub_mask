from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path("geo/", include("geo.urls", namespace="geo")),
    path("address/", include("address.urls", namespace="address")),
    path("stock/", include("stock.urls", namespace="stock")),
]
