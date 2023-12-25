from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # method 1: return http response
    return HttpResponse("Hello From Django")

def index2(request):
    # method 2: return html files
    return render(request, "index.html")



