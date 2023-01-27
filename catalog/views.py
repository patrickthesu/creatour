from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from .models import TouristProduct

from account import services as account

from .forms import EthapForm

class TouristProductListView (generic.ListView): 
    model = TouristProduct
    context_object_name = "product_list"
    template_name = "touristProductList.html"

class AuthorListView (generic.ListView): 
    model = User 
    context_object_name = "authorList"
    template_name = "authorList.html"

def createEthapView (request): 
    form = EthapForm
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["creator"] = request.user
        form = EthapForm(request.POST, request.FILES )
        request.POST._mutable = False
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse ( "profile" ))
    return render ( request, "createEthap.html", context = {"form": form})

def createProductView (request):
    return render ( request, "createProduct.html" )

def editProductView (request):
    return render ( request, "editProduct.html" )

def productDetailView (request):
    return render ( request, "productDetails.html")


