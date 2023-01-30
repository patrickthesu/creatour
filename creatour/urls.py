from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ("", include ("catalog.urls")),
    path ("admin/", admin.site.urls, name = "admin"),
    path ("account/", include("account.urls")),
]
