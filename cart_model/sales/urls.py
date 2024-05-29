from django.urls import path
from admin_panel.views import *

urlpatterns = [
    path("", Home.as_view(), name="sales_home"),
    #     Profile
    path("profile/", Profile.as_view(), name="sales_profile"),
    #     Change password
    path("changepwd/", ChangePwd.as_view(), name="sales_changepwd"),
    # Purchase
    path("purchase/", Purchase.as_view(), name="sales_purchase"),
    path("purchase_detail/<pk>/", PurchaseDetail.as_view(),
         name="sales_purchase_detail"),
    path("purchase_update/<pk>/", PurchaseUpdate.as_view(),
         name="sales_purchase_update"),
]
