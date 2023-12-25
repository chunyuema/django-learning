from django.urls import path
from djangoModels.views import *

urlpatterns = [
    path("users/", getUsers, name="users"),
]
