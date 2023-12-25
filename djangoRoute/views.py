from django.http import HttpResponse
from django.shortcuts import render
from djangoRoute.models import *

# Create your views here.
def index(request):
    # method 2: return html files
    return render(request, "index.html")

def user_list(request):
    print("Getting all the users ...")
    users = UserModel.objects.all()
    print("Finished getting all users ...", users)

    # Passing arguments into url
    return render(request, "users.html", {"users": users})



