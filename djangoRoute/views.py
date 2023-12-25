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


def user_detail(request, user_id):
    print("Getting user information for ", user_id)
    user = UserModel.objects.get(pk=user_id)
    print("Finishe getting user information for ", user.name)

    # Passing argument into url
    return render(request, "user_detail.html", {"user": user})


def test(request, a, b):
    return HttpResponse(f'a:{a} - b:{b}')



