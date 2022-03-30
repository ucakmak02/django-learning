from datetime import datetime

from django.shortcuts import render


def index(request):
    date = datetime.now()
    return render(request, "index.html", context={"name": "Ugur", "date": date})
