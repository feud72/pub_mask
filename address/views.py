import os

from django.shortcuts import render, redirect
from django.urls import reverse

import requests

from .forms import SearchForm

API_URL = os.environ.get("API_URL")

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


def addressView(request, address=None):
    if request.method == "GET":
        form = SearchForm()
        if address is None:
            address = QUERY
        raw = requests.get(f"{API_URL}{ENDPOINT}?address={address}")
        context = raw.json() if raw.status_code == 200 else {}
        return render(request, "address.html", {"context": context, "form": form})
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            return redirect(reverse("address:address", args=[address] ))
        else:
            form = SearchForm()
            return redirect(reverse("address:index"))