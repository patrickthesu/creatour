from django.urls import path
from . import views

urlpatterns = [
    path ("", views.profileView, name = "profile" ),
    path ("login/", views.loginView, name = "login" ),
    path ("signin/", views.signinView, name = "signin"),
    path ("logout/", views.logoutView, name = "logout" ),
    path ("password-reset", views.resetPasswordView, name = "passwordReset"),
    path ("edit/", views.editProfileView, name = "editProfile"),
    path ("stats/", views.getProfileStatsView, name = "profileStats"),
    path ("author/<int:authorId>", views.getAuthorDetails, name = "authorDetails"),
    path ("forbidden/", views.forbidden, name = "forbidden")
]
