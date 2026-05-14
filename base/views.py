from django.shortcuts import render
from base.models import Person

# Create your views here.


def index(request):
    name = None
    email = None
    message = None
    if request.method == "POST":
        name =request.POST.get("name")
        email =request.POST.get("email")
        message =request.POST.get("message")
    
    person = Person.objects.create(name= name, email=email, message=message)
    person.save()

    return render(request, "index.html")
