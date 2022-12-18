from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Product
#
from .models import Upload



# Create your views here.

def index(request):
    context = {
        'products':Product.objects.all()
    }
    return render( request , 'pages/index.html' ,context)

def about(request):
    return render( request , 'pages/about.html' )

#def send_message(request):
#   return render(request,'pages/contact.html',{})


#///////////////////////
#speech


