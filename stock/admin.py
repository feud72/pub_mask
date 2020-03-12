from django.contrib import admin

from .models import Store, Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("store", "status", "created_at")
    ordering = ("-created_at",)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
