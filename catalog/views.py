from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from .models import TouristProduct, Review

from account import services as account

from .forms import EthapForm, TouristProductForm, ReviewForm

def index (request):    
    return HttpResponseRedirect(reverse ("profile"))

class TouristProductListView (generic.ListView): 
    model = TouristProduct
    context_object_name = "product_list"
    template_name = "touristProductList.html"

@account.group_required
def deleteReviewView (request, reviewPk):
    review = Review.objects.get(pk = reviewPk)
    touristProduct = TouristProduct.objects.get ( pk = review.touristProduct.pk )
    if review.user.pk == request.user.pk:
        review.delete()
    return  HttpResponseRedirect(touristProduct.getAbsoluteUrl())

@account.group_required
def touristProductView (request, productId):
    form = ReviewForm

    product = TouristProduct.objects.get(pk = productId)
    reviews = Review.objects.all().filter(touristProduct__pk = productId)

    #print (f"{Review.objects.all().delete()}")

    consumer = False
    if "consumer" in request.user.groups.all()[0].name: consumer = True
 
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["user"] = f'{request.user.pk}'
        request.POST["touristProduct"] = f'{product.pk}'
        form = ReviewForm(request.POST)
        request.POST._mutable = False
        if form.is_valid(): 
            form.save()
    context = {"product": product, "reviews": reviews, "form": form, "consumer": consumer}
    return render ( request, "productDetails.html", context = context)

class AuthorListView (generic.ListView): 
    model = User
    context_object_name = "authorList"
    template_name = "authorList.html"


@account.login_required
def createEthapView (request): 
    form = EthapForm
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["creator"] = request.user
        form = EthapForm(request.POST, request.FILES )
        request.POST._mutable = False
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse ("profile"))
    return render ( request, "createEthap.html", context = {"form": form})

def createProductView (request):
    form = TouristProductForm
    if request.method == "POST":
        form = TouristProductForm(request.POST, request.FILES )
        request.POST._mutable = True
        request.POST["creator"] = request.user
        form = TouristProductForm(request.POST, request.FILES )
        request.POST._mutable = False 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse ( "profile" ))
    return render ( request, "createProduct.html", context = {"form":form} )

@account.login_required
def editProductView (request):
    return render ( request, "editProduct.html" )
