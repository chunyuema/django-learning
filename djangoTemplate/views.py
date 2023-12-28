from django.shortcuts import render

# Create your views here.
def djangoTemplateIndex(request):
    data = {
        "name": "chunyue",
        "age": 25,
        "hobbies": ["chess", "coding"],
        "address": {"city": "seattle", "state": "WA"},
    }
    return render(request, "index-django-template.html", data)
