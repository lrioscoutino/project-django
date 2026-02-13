from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_user(request):
    return HttpResponse("Hello World")

def inicio(request):
    context = {
        "name":"Roberto Carlos",
        "email":"r@gmail.com",
        "age": 35,
        "resumen":[3,5,67,7,8,8]
    }
    return render(request, "base.html",context=context)