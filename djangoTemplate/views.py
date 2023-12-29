from django.shortcuts import render

# Create your views here.
def djangoTemplateIndex(request):
    data = {
        "name": "chunyue",
        "age": 25,
        "hobbies": ["chess", "swimming", "coding"],
        "address": {"city": "seattle", "state": "WA"},
        "foobar": [["1", "2", "3"],
                   ["4", "5", "6"],
                   ["7", "8", "9"]]
    }
    return render(request, "index-django-template.html", data)
