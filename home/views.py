import os

from django.shortcuts import render, redirect
from django.urls import reverse

import requests

from address.forms import SearchForm

def homeView(request):
    if request.method == "GET":
        form = SearchForm()
        return render(request, "home.html", {"form": form})
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            return redirect(reverse("address:address", args=[address] ))
        else:
            form = SearchForm()
            return redirect(reverse("home:index"))        
