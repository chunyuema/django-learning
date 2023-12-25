from django.urls import path, re_path
from djangoRoute.views import *

urlpatterns = [
    path('index/', index, name = 'index'),
    path('userlist/', user_list, name = 'userlist'),

    # passing one argument
    path('userdetail/<int:user_id>/', user_detail, name = 'userdetail'),

    # passing multiple arguments
    path('test/<int:a>/<int:b>', test, name = 'test'),

    # using regular expression
    re_path(r'test2/(?P<a>\d+)/(?P<b>\d+)/', test, name = 'test2')
]
