from django.urls import path
from admin_panel.views import *

urlpatterns = [
    path("", Home.as_view(), name="stock_home"),
    # Category
    path("category/", Category.as_view(), name="stock_category"),
    path("category_create/", CategoryCreate.as_view(),
         name="stock_category_create"),
    path("category_detail/<pk>/", CategoryDetail.as_view(),
         name="stock_category_detail"),
    path("category_update/<pk>/", CategoryUpdate.as_view(),
         name="stock_category_update"),
    path("category_delete/<pk>/", CategoryDelete.as_view(),
         name="stock_category_delete"),
    # Image
    path("image/", Image.as_view(), name="stock_image"),
    path("image_create/", ImageCreate.as_view(),
         name="stock_image_create"),
    path("image_detail/<pk>/", ImageDetail.as_view(),
         name="stock_image_detail"),
    path("image_update/<pk>/", ImageUpdate.as_view(),
         name="stock_image_update"),
    path("image_delete/<pk>/", ImageDelete.as_view(),
         name="stock_image_delete"),
    path("image_get/<id>/", getImage,
         name="stock_image_get"),
    # Product
    path("product/", Product.as_view(), name="stock_product"),
    path("product_create/", ProductCreate.as_view(),
         name="stock_product_create"),
    path("product_detail/<pk>/", ProductDetail.as_view(),
         name="stock_product_detail"),
    path("product_update/<pk>/", ProductUpdate.as_view(),
         name="stock_product_update"),
    path("product_delete/<pk>/", ProductDelete.as_view(),
         name="stock_product_delete"),

    # Stock
    path("stock/", Stock.as_view(), name="stock_stock"),
    path("stock_create/", StockCreate.as_view(),
         name="stock_stock_create"),
    path("stock_detail/<pk>/", StockDetail.as_view(),
         name="stock_stock_detail"),
    path("stock_update/<pk>/", StockUpdate.as_view(),
         name="stock_stock_update"),
    path("stock_delete/<pk>/", StockDelete.as_view(),
         name="stock_stock_delete"),

    #     Profile
    path("profile/", Profile.as_view(), name="stock_profile"),
    #     Change password
    path("changepwd/", ChangePwd.as_view(), name="stock_changepwd"),
    # Purchase
    path("purchase/", Purchase.as_view(), name="stock_purchase"),
    path("purchase_detail/<pk>/", PurchaseDetail.as_view(),
         name="stock_purchase_detail"),
    path("purchase_update/<pk>/", PurchaseUpdate.as_view(),
         name="stock_purchase_update"),
]
