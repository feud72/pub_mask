import os

from django.shortcuts import render, redirect
from django.urls import reverse

import requests

from .forms import SearchForm

MASK_API_URL = os.environ.get("API_URL")

ADDR_API_URL = os.environ.get("ADDR_API_URL")
ADDR_API_KEY = os.environ.get("ADDR_API_KEY")

ENDPOINT = "/storesByAddr/json"

QUERY = "충청남도 아산시 탕정면"


def searchView(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            return redirect(reverse("address:address", address=address))
        else:
            form = SearchForm()
            return redirect(reverse("address:index"))


def processingKeyword(keyword=None):
    if keyword is None:
        keyword = "서울특별시 강남구 신사동"
    addr_raw = requests.get(
        url=ADDR_API_URL,
        params={
            "keyword": keyword,
            "confmKey": ADDR_API_KEY,
            "currentPage": 1,
            "countPerPage": 10,
            "resultType": "json",
        },
    )
    if addr_raw.status_code == 200:
        try:
            addr = addr_raw.json().get("results").get("juso")[0]
            result = f'{addr.get("siNm")} {addr.get("sggNm")} {addr.get("emdNm")}'
            return result
        except Exception:
            return "서울특별시 강남구 신사동"
    else:
        return "서울특별시 강남구 신사동"


def addressView(request, address=None):
    if request.method == "GET":
        form = SearchForm()
        raw = requests.get(f"{MASK_API_URL}{ENDPOINT}?address={address}")
        context = raw.json() if raw.status_code == 200 else {}
        return render(request, "address.html", {"context": context, "form": form})
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            address = processingKeyword(address)
            return redirect(reverse("address:address", args=[address]))
        else:
            form = SearchForm()
            return redirect(reverse("address:index"))
