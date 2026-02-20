from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from users.models import Product

# Create your views here.
def get_user(request):
    return HttpResponse("Hello World")

def inicio(request):
    products = Product.objects.all()
    context = {
        "name":"Roberto Carlos",
        "email":"r@gmail.com",
        "age": 35,
        "resumen":[3,5,67,7,8,8],
        "products":products
    }
    return render(request, "base.html",context=context)