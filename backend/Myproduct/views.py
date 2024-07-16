from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Product
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'page1.html',{})

class Productlist(View):
    def get(self,request):
        produits=Product.objects.all()
        return render(request,'listProduct.html',{'prods':produits})



class Vehicule(View):
    def get(self,request):
        voitu=request.GET.get('voiture')
        var1=Product.objects.filter(category=voitu)
        return render(request,'vehicule.html',{'context':var1})

class Immobilier(View):
    def get(self,request):
        return render(request,'immobilier.html',{})

class Informatique(View):
    def get(self,request):
        return render(request,'informatique.html',{})

class Loisir(View):
    def get(self,request):
        return render(request,'loisir.html',{})


