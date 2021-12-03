from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return HttpResponse('Hello Beautiful')


def new(request):
    return HttpResponse('New Products')

