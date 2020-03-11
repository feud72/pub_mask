import os

from django.shortcuts import render

import requests

API_URL = os.environ.get("API_URL")

ENDPOINT = "/storesByGeo/json"


def geoView(request, lat=None, lng=None):
    if lat is None or lng is None:
        lat, lng = 37.517235, 127.047325
    raw = requests.get(f"{API_URL}{ENDPOINT}?lat={lat}&lng={lng}")
    context = raw.json() if raw.status_code == 200 else {}
    return render(request, "geo.html", {"context": context})
