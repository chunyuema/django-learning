from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from djangoRoute.models import *


# Create your views here.
def index(request):
    # method 2: return html files
    return render(request, "index-django-template.html")


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


'''
The following are examples of redirecting and reverse parsing through views
- redirect: used for redirecting from one url to another
- reverse: used to do reverse parsing
    - note that if you declared namespace, please specify from the reverse
'''


def my_redirect(request):
    # redirect to google site
    return redirect('https://www.google.com')


def redirect_to_user_list(request):
    return redirect('/djangoRoute/userlist/')


def redirect_to_user_detail(request):
    # use reverse parsing here, note that we use namespace here
    # this is because we have declared the namespace in the djangoProject1
    # return redirect(reverse('djangoRoute:userdetail', args=(2,)))

    # another way of passing in the argument through keyword
    return redirect(reverse('djangoRoute:userdetail', kwargs={'user_id': 2}))
