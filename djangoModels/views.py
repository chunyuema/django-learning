from django.shortcuts import render

from djangoModels.models import UserModel


# Create your views here.
def getUsers(request):
    users = UserModel.objects.all()

    # Passing arguments into url
    return render(request, "users.html", {"users": users})
