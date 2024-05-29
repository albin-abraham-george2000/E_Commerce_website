from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="guest_home"),
    path("contact/", Contact.as_view(), name="guest_contact"),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("signout/", SignOut.as_view(), name="signout"),
]
