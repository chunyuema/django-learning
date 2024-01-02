from django.contrib import admin

# Register your models here.
from djangoModels.models import *

# Register the models in order to manage the models
admin.site.register(PersonModel)
admin.site.register(UserModel)
