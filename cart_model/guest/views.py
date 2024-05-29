from django.shortcuts import render, redirect
from django.views import View
from admin_panel.models import UserInfo
from django.contrib.auth.models import Group
from .forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password
from admin_panel.models import Stock, Category
from django.db.models import Q


class Home(View):
    def get(self, req):
        filt = req.GET.get("f", "")
        stocks = Stock.objects.filter(
            Q(product__item__contains=filt) |
            Q(product__category__cat_name__contains=filt)
        )
        cats = Category.objects.all()
        return render(req, "guest/home.html", {"stocks": stocks, "cats": cats})

# using class


class Contact(View):
    def get(self, req):
        return render(req, "guest/contact.html", {})


class Login(View):
    def get(self, req):
        return render(req, "guest/login.html", {})

    def post(self, req):
        msg = ""
        frm = LoginForm(req.POST)
        if not frm.is_valid():
            return render(req, "guest/login.html", {"frm": frm, "msg": msg})
        usr = UserInfo.objects.filter(username=req.POST["email"])
        password = req.POST["password"]

        if usr:
            if check_password(password, usr[0].password):
                grp = usr[0].groups.all()[0].name.lower()
                req.session["name"] = f"{usr[0].first_name} {usr[0].last_name}"
                req.session["username"] = usr[0].username
                req.session["uid"] = usr[0].id
                req.session["address"] = usr[0].address
                req.session["group"] = grp
                p = f"{grp}/layout.html"
                if grp.lower() == "admin":
                    p = f"admin_panel/layout.html"
                req.session["path"] = p
                return redirect(grp + "_home")
            else:
                msg = "Invalid Password ?"
        else:
            msg = "Invalid Username ?"
        return render(req, "guest/login.html", {"msg": msg})


class Register(View):
    def get(self, req):
        return render(req, "guest/register.html", {})

    def post(self, req):
        msg = "Registered Successfully !!!"
        try:
            ui = UserInfo(
                first_name=req.POST["first_name"],
                last_name=req.POST["last_name"],
                email=req.POST["email"],
                username=req.POST["email"],
                password=make_password(req.POST["password"]),
                address=req.POST["address"],
                contact=req.POST["contact"],
            )
            grp = Group.objects.get(name="Customer")
            if grp:
                ui.save()
                ui.groups.add(grp)
                ui.save()
            else:
                msg = "Customer group not found !"

        except Exception as e:
            msg = str(e)
        return render(req, "guest/register.html", {"msg": msg})


class SignOut(View):
    def get(self, req):
        del req.session["name"]
        del req.session["username"]
        del req.session["group"]
        return redirect("login")
