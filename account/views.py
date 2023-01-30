from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import services
from . import forms

def forbidden ( request ):
    return render ( request, "forbidden.html", context = {} )

def signinView ( request ):
    form = forms.SigninForm
    if request.method == "POST":
        form = forms.SigninForm (request.POST)
        if not form.is_valid() or not services.signin(form): form.add_error(None, "Ошибка регистрации")
        return HttpResponseRedirect(reverse("login"))

    return render ( request, "signin.html", context = {"form": form, } )

def loginView ( request ):

    form = forms.LoginForm
    if request.method == "POST":
        form = forms.LoginForm (request.POST)
        if form.is_valid():
            if services.login ( request, **form.cleaned_data ): return HttpResponseRedirect(reverse("profile"))
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
    return render ( request, "account.html", context = {} )

def consumerView (request): 
    return render ( request, "account.html", context = {} )

@services.login_required
def profileView (request):
    try:
        group = request.user.groups.all()[0]
    except:
        return render ( request, "account.html", context = {} )

    if services.isUserAuthor ( request.user ):
        return authorView ( request )
    if group.name == "consumer":
        return consumerView ( request )
    if group.name == "producer":
        return producerView ( request )

    return render ( request, "account.html", context = {} )

@services.login_required
def editProfileView (request):
   return render ( request, "editProfile.html", context = {} )

def getAuthorDetails ( request, authorId ):
    pass

def resetPasswordView (request):
    pass

#@services.login_required(reverse('login'))
def getProfileStatsView (request):
    pass
