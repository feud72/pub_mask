import os

from django.shortcuts import render

from .models import Store, Stock

import requests

MASK_API_URL = os.environ.get("API_URL")
ENDPOINT = "/storesByAddr/json"


def getJSON(address):
    raw = requests.get(f"{MASK_API_URL}{ENDPOINT}?address={address}")
    result = raw.json() if raw.status_code == 200 else {}
    return result


def getDataView(request):
    addr_list = ["충청남도 천안시 서북구 불당동", "충청남도 아산시 탕정면", "충청남도 아산시 배방읍", "충청남도 아산시 음봉면"]
    for addr in addr_list:
        raw = getJSON(addr)
        resp = raw.get("stores")
        for store in resp:
            obj, created = Store.objects.get_or_create(name=store["name"], region=addr)
            if created is False:
                if Stock.objects.filter(store=obj.id).exists():
                    last_item = (
                        Stock.objects.filter(store=obj.id).order_by("created_at").last()
                    )
                    if last_item.status == store["remain_stat"]:
                        continue
            Stock.objects.create(store=obj, status=store["remain_stat"])
    return render(request, "stock/get_data.html")


def storeListView(request):
    queryset = Store.objects.all()
    tang = queryset.filter(region__contains="탕정면")
    bul = queryset.filter(region__contains="불당동")
    bae = queryset.filter(region__contains="배방읍")
    eum = queryset.filter(region__contains="음봉면")
    return render(
        request,
        "stock/list_store.html",
        {"querydict": {"탕정면": tang, "불당동": bul, "배방읍": bae, "음봉면": eum}},
    )


def storeDetailView(request, store):
    queryset = Stock.objects.filter(store__name=store).order_by("-created_at")
    return render(
        request, "stock/detail_store.html", {"store": store, "stock": queryset}
    )
