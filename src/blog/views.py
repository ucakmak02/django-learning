from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def article(request, num_article, title):
    print(num_article, title)
    return render(request, "blog/article.html", context={"num": num_article, "title": title})
