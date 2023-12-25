from django.urls import path
from djangoRoute.views import *

urlpatterns = [
    path('index/', index, name = 'index'),
    path('userlist/', user_list, name = 'userlist'),
    path('userdetail/<int:user_id>/', user_detail, name = 'userdetail')
]
