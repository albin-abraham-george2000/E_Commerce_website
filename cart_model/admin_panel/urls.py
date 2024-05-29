from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="admin_home"),
    # Category
    path("category/", Category.as_view(), name="admin_category"),
    path("category_create/", CategoryCreate.as_view(),
         name="admin_category_create"),
    path("category_detail/<pk>/", CategoryDetail.as_view(),
         name="admin_category_detail"),
    path("category_update/<pk>/", CategoryUpdate.as_view(),
         name="admin_category_update"),
    path("category_delete/<pk>/", CategoryDelete.as_view(),
         name="admin_category_delete"),
    # Image
    path("image/", Image.as_view(), name="admin_image"),
    path("image_create/", ImageCreate.as_view(),
         name="admin_image_create"),
    path("image_detail/<pk>/", ImageDetail.as_view(),
         name="admin_image_detail"),
    path("image_update/<pk>/", ImageUpdate.as_view(),
         name="admin_image_update"),
    path("image_delete/<pk>/", ImageDelete.as_view(),
         name="admin_image_delete"),
    path("image_get/<id>/", getImage,
         name="admin_image_get"),
    # Product
    path("product/", Product.as_view(), name="admin_product"),
    path("product_create/", ProductCreate.as_view(),
         name="admin_product_create"),
    path("product_detail/<pk>/", ProductDetail.as_view(),
         name="admin_product_detail"),
    path("product_update/<pk>/", ProductUpdate.as_view(),
         name="admin_product_update"),
    path("product_delete/<pk>/", ProductDelete.as_view(),
         name="admin_product_delete"),

    # Stock
    path("stock/", Stock.as_view(), name="admin_stock"),
    path("stock_create/", StockCreate.as_view(),
         name="admin_stock_create"),
    path("stock_detail/<pk>/", StockDetail.as_view(),
         name="admin_stock_detail"),
    path("stock_update/<pk>/", StockUpdate.as_view(),
         name="admin_stock_update"),
    path("stock_delete/<pk>/", StockDelete.as_view(),
         name="admin_stock_delete"),

    # User
    path("user/", User.as_view(), name="admin_user"),
    path("user_create/", UserCreate.as_view(),
         name="admin_user_create"),
    path("user_detail/<pk>/", UserDetail.as_view(),
         name="admin_user_detail"),
    path("user_update/<pk>/", UserUpdate.as_view(),
         name="admin_user_update"),
    path("user_delete/<pk>/", UserDelete.as_view(),
         name="admin_user_delete"),
    #     Profile
    path("profile/", Profile.as_view(), name="admin_profile"),
    #     Change password
    path("changepwd/", ChangePwd.as_view(), name="admin_changepwd"),
    # Purchase
    path("purchase/", Purchase.as_view(), name="admin_purchase"),
    path("purchase_detail/<pk>/", PurchaseDetail.as_view(),
         name="admin_purchase_detail"),
    path("purchase_update/<pk>/", PurchaseUpdate.as_view(),
         name="admin_purchase_update"),
]
