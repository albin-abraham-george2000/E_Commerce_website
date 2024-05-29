from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import admin_panel.models as am
from django.db.models import Q


class Home(View):
    def get(self, req):
        filt = req.GET.get("f", "")
        stocks = am.Stock.objects.filter(
            Q(product__item__contains=filt) |
            Q(product__category__cat_name__contains=filt)
        )
        cats = am.Category.objects.all()
        return render(req, "customer/home.html", {"stocks": stocks, "cats": cats})

# using class


class Contact(View):
    def get(self, req):
        return render(req, "customer/contact.html", {})


class Shop(ListView):
    model = am.Stock
    template_name = "customer/shop.html"
    context_object_name = "datas"
    paginate_by = 3

    def get_queryset(self):
        self.filter = self.request.GET.get("f", "")
        self.sort = self.request.GET.get("s", "-stock_date")
        self.price = float(self.request.GET.get("p", 0))

        datas = am.Stock.objects.filter(
            Q(product__item__contains=self.filter) |
            Q(product__category__cat_name__contains=self.filter)
        ).order_by(self.sort)

        if self.price > 0:
            datas = datas.filter(price__lte=self.price)
        return datas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = am.Category.objects.all().order_by('cat_name')
        context["f"] = self.filter
        context["s"] = self.sort
        context["p"] = self.price

        return context


class Cart(ListView):
    model = am.Cart
    template_name = "customer/cart.html"
    context_object_name = "datas"

    def get_queryset(self):
        st_id = int(self.request.GET.get("id", 0))
        delid = int(self.request.GET.get("delid", 0))
        uid = self.request.session["uid"]
        if st_id != 0:
            c = am.Cart.objects.filter(user_id=uid, stock_id=st_id)
            if len(c) == 0:
                c = am.Cart(user_id=uid, stock_id=st_id)
                c.save()
        c = am.Cart.objects.filter(id=delid)
        if len(c) != 0:
            c[0].delete()
        datas = am.Cart.objects.filter(user_id=uid)
        self.request.session["cart"] = len(datas)
        return datas


class Detail(View):
    def get(self, req):
        return render(req, "customer/detail.html", {})


class Checkout(ListView):
    model = am.Purchase
    template_name = "customer/checkout.html"
    context_object_name = "datas"

    def post(self, req):
        cart_id = req.POST.getlist("cart_id")
        qty = req.POST.getlist("quantity")
        uid = req.session["uid"]
        if len(cart_id) != 0:
            b = am.Bill(user_id=uid)
            b.save()
            for i in range(0, len(cart_id)):
                if int(qty[i]) != 0:
                    c = am.Cart.objects.get(id=cart_id[i])
                    s = am.Stock.objects.get(id=c.stock.id)
                    p = am.Purchase(
                        bill=b, stock=s, quantity=qty[i], status_id=1

                    )
                    p.save()
                    c.delete()

        datas = am.Purchase.objects.filter(bill__user_id = uid)
        return render(req, "customer/checkout.html", {"datas": datas})
