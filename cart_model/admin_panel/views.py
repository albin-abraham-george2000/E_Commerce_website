from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
import admin_panel.models as m
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q


class Home(ListView):
    model = m.Stock
    template_name = "admin_panel/home.html"
    context_object_name = "datas"
    paginate_by = 3

    def get_queryset(self):
        self.filt = self.request.GET.get("f", "")
        self.col = self.request.GET.get("c", "price")
        self.dire = self.request.GET.get("d", "asc")
        if self.dire == 'desc':
            self.col = "-" + self.col
        datas = m.Stock.objects.filter(
            Q(product__item__contains=self.filt) |
            Q(product__category__cat_name__contains=self.filt)
        ).order_by(self.col)
        return datas

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont["filt"] = self.filt
        cont["c"] = self.col.replace("-", "")
        cont["d"] = self.dire
        return cont

# Category Starts


class Category(ListView):
    model = m.Category
    template_name = "admin_panel/category.html"
    context_object_name = "datas"


class CategoryDetail(DetailView):
    model = m.Category
    template_name = "admin_panel/category_detail.html"
    context_object_name = "datas"


class CategoryCreate(CreateView):
    model = m.Category
    template_name = "admin_panel/category_create.html"
    fields = ["cat_name"]
    success_url = "/admin_panel/category/"


class CategoryUpdate(UpdateView):
    model = m.Category
    template_name = "admin_panel/category_update.html"
    fields = ["cat_name"]
    success_url = "/admin_panel/category/"
    context_object_name = "datas"


class CategoryDelete(DeleteView):
    model = m.Category
    template_name = "admin_panel/category_delete.html"
    success_url = "/admin_panel/category/"
    context_object_name = "datas"
# Category Ends

# Image Starts


class Image(ListView):
    model = m.Image
    template_name = "admin_panel/image.html"
    context_object_name = "datas"


class ImageDetail(DetailView):
    model = m.Image
    template_name = "admin_panel/image_detail.html"
    context_object_name = "datas"


class ImageCreate(CreateView):
    model = m.Image
    template_name = "admin_panel/image_create.html"
    fields = ["image", "descr"]
    success_url = "/admin_panel/image/"


class ImageUpdate(UpdateView):
    model = m.Image
    template_name = "admin_panel/image_update.html"
    fields = ["image", "descr"]
    success_url = "/admin_panel/image/"
    context_object_name = "datas"


class ImageDelete(DeleteView):
    model = m.Image
    template_name = "admin_panel/image_delete.html"
    success_url = "/admin_panel/image/"
    context_object_name = "datas"


def getImage(req, id):
    img = m.Image.objects.get(id=id)
    return HttpResponse(img.image.url)

# Image Ends

# Product Starts


class Product(ListView):
    model = m.Product
    template_name = "admin_panel/product.html"
    context_object_name = "datas"


class ProductDetail(DetailView):
    model = m.Product
    template_name = "admin_panel/product_detail.html"
    context_object_name = "datas"


class ProductCreate(CreateView):
    model = m.Product
    template_name = "admin_panel/product_create.html"
    fields = ["item", "descr", "category", "image"]
    success_url = "/admin_panel/product/"


class ProductUpdate(UpdateView):
    model = m.Product
    template_name = "admin_panel/product_update.html"
    fields = ["item", "descr", "category", "image"]
    success_url = "/admin_panel/product/"
    context_object_name = "datas"


class ProductDelete(DeleteView):
    model = m.Product
    template_name = "admin_panel/product_delete.html"
    success_url = "/admin_panel/product/"
    context_object_name = "datas"
# Product Ends


# Stock Starts


class Stock(ListView):
    model = m.Stock
    template_name = "admin_panel/stock.html"
    context_object_name = "datas"


class StockDetail(DetailView):
    model = m.Stock
    template_name = "admin_panel/stock_detail.html"
    context_object_name = "datas"


class StockCreate(CreateView):
    model = m.Stock
    template_name = "admin_panel/stock_create.html"
    fields = ["product", "price", "quantity",
              "stock_date", "mfg_date", "exp_date"]
    success_url = "/admin_panel/stock/"


class StockUpdate(UpdateView):
    model = m.Stock
    template_name = "admin_panel/stock_update.html"
    fields = ["product", "price", "quantity",
              "stock_date", "mfg_date", "exp_date"]
    success_url = "/admin_panel/stock/"
    context_object_name = "datas"


class StockDelete(DeleteView):
    model = m.Stock
    template_name = "admin_panel/stock_delete.html"
    success_url = "/admin_panel/stock/"
    context_object_name = "datas"
# Stock Ends


# User Starts


class User(ListView):
    model = m.UserInfo
    template_name = "admin_panel/user.html"
    context_object_name = "datas"


class UserDetail(DetailView):
    model = m.UserInfo
    template_name = "admin_panel/user_detail.html"
    context_object_name = "datas"


class UserCreate(CreateView):
    model = m.UserInfo
    template_name = "admin_panel/user_create.html"
    fields = ["first_name", "last_name", "email",
              "address", "contact", "groups", "username", "password"]
    success_url = "/admin_panel/user/"

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = m.UserInfo
    template_name = "admin_panel/user_update.html"
    fields = ["first_name", "last_name", "email",
              "address", "contact", "groups", "username"]
    success_url = "/admin_panel/user/"
    context_object_name = "datas"


class UserDelete(DeleteView):
    model = m.UserInfo
    template_name = "admin_panel/user_delete.html"
    success_url = "/admin_panel/user/"
    context_object_name = "datas"
# User Ends


class Profile(View):
    def get(self, req):
        un = req.session["username"]
        datas = m.UserInfo.objects.get(username=un)
        return render(req, 'admin_panel/profile.html', {"datas": datas})

    def post(self, req):
        un = req.session["username"]
        datas = m.UserInfo.objects.get(username=un)
        datas.first_name = req.POST["first_name"]
        datas.last_name = req.POST["last_name"]
        datas.contact = req.POST["contact"]
        datas.email = req.POST["email"]
        datas.address = req.POST["address"]
        datas.save()
        return render(req, 'admin_panel/profile.html', {"datas": datas})


class ChangePwd(View):
    def get(self, req):
        return render(req, 'admin_panel/changepwd.html', {})

    def post(self, req):
        opwd = req.POST["opwd"]
        npwd = req.POST["npwd"]
        msg = ""

        un = req.session["username"]
        datas = m.UserInfo.objects.get(username=un)
        if check_password(opwd, datas.password):
            datas.password = make_password(npwd)
            datas.save()
            msg = "Password Changed Successfully !"
        else:
            msg = "Invalid old Password ?"
        return render(req, 'admin_panel/changepwd.html', {"msg": msg})


# Purchase Starts

class Purchase(ListView):
    model = m.Purchase
    template_name = "admin_panel/purchase.html"
    context_object_name = "datas"


class PurchaseDetail(DetailView):
    model = m.Purchase
    template_name = "admin_panel/purchase_detail.html"
    context_object_name = "datas"


class PurchaseUpdate(UpdateView):
    model = m.Purchase
    template_name = "admin_panel/purchase_update.html"
    fields = ["status"]
    success_url = "/admin_panel/purchase/"
    context_object_name = "datas"

# Purchase Ends
