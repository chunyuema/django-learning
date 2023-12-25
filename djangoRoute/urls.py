from django.urls import path
from djangoRoute.views import *

urlpatterns = [
    path('index/', index, name = 'index'),
    path('userlist/', user_list, name = 'userlist')
]
