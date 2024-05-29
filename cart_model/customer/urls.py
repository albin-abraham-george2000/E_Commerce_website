from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="customer_home"),
    path("contact/", Contact.as_view(), name="customer_contact"),
    path("shop/", Shop.as_view(), name="shop"),
    path("cart/", Cart.as_view(), name="cart"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("detail/", Detail.as_view(), name="detail"),
]
