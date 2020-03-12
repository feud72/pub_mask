import os
import json

from django.shortcuts import render

from .models import Store, Stock

import requests

MASK_API_URL = os.environ.get("API_URL")
ENDPOINT = "/storesByAddr/json"


def getJSON(address):
    raw = requests.get(f"{MASK_API_URL}{ENDPOINT}?address={address}")
    result = raw.json() if raw.status_code == 200 else {}
    return result


def jsonToObj(jsonObj):
    data = jsonObj.get("stores")
    result = json.loads(data)
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
                        Stock.objects.filter(store=obj.id)
                        .order_by("-created_at")
                        .last()
                    )
                    if last_item.status == store["remain_stat"]:
                        continue
            Stock.objects.create(store=obj, status=store["remain_stat"])
    return render(request, "stock/list_store.html")


def storeListView(request):
    queryset = Store.objects.all()
    return render(request, "stock/list_store.html", {"stores": queryset})


def storeDetailView(request, store):
    queryset = Stock.objects.filter(store__name=store).order_by("-created_at")
    return render(
        request, "stock/detail_store.html", {"store": store, "stock": queryset}
    )
