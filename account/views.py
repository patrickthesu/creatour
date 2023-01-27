from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from . import services
from . import forms

def signinView ( request ):
    form = forms.SigninForm

    if request.method == "POST":
        form = forms.SigninForm (request.POST)
        if not form.is_valid() or not services.signin(form): form.add_error(None, "Ошибка регистрации")

    return render ( request, "signin.html", context = {"form": form, } )

def loginView ( request ):
    form = forms.LoginForm
    if request.method == "POST":
        form = forms.LoginForm (request.POST)
        if not form.is_valid():
            if services.login ( request, **form.cleaned_data ): return HttpResponseRedirect(reverse("index") )            
        form.add_error(None, "Неправильное имя и/или пароль")

    return render ( request, "login.html", context = {"form": form, } )

def logoutView (request):
    if services.logout ( request ): return render ( request, "loggedOut.html" )

    return render ( request, "loggedOut.html", context = {"error": True} )

def authorView (request):
    if request.method == "POST":
        pass
    return render ( request, "author.html" )


def producerView (request):
    pass

def consumerView (request):
    pass

@login_required()
def profileView (request):

    group = request.user.groups.all()[0]

    if services.isUserAuthor ( request.user ):
        return authorView ( request )
    if group.name == "consumer":
        return consumerView ( request )
    if group.name == "producer":
        return producerView ( request )

    return render ( request, "account.html", context = {} )

def resetPasswordView (request):
    pass

@login_required()
def getProfileStatsView (request):
    pass
