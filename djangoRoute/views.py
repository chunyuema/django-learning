from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # method 2: return html files
    return render(request, "index.html")

def user_list(request):
    return render(request, "users.html")



