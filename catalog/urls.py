from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path ( "", views.TouristProductListView.as_view(), name = "index" ),
    path ( "products/", RedirectView.as_view(url="", permanent=True ), name = "product-list"),
    path ( "authors/", views.AuthorListView.as_view() , name = "creatures-list" ),
    path ( "ethaps/create", views.createEthapView, name = "createEthap" ),
    path ( "product/create", views.createProductView, name = "createProduct" ),
    path ( "product/<int:productId>", views.productDetailView, name = "productDetails" ),
    path ( "product/<int:productId>/edit", views.editProductView, name = "editProduct" ),
    ]
