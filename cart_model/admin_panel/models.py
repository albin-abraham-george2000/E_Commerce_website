from django.db import models as m
from django.contrib.auth.models import User

# UserInfo (inherits User):-  address, contact


class UserInfo(User):
    address = m.CharField(max_length=100)
    contact = m.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "userinfo"

# # Catagory:- id#, cat_name


class Category(m.Model):
    id = m.AutoField(primary_key=True)
    cat_name = m.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.cat_name}"

    class Meta:
        db_table = "category"
        ordering = ("cat_name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Image (id#, image, descr)


class Image(m.Model):
    id = m.AutoField(primary_key=True)
    image = m.ImageField(upload_to="uploads/")
    descr = m.CharField(max_length=50)

    def __str__(self):
        return f"{self.descr}"

    class Meta:
        db_table = "image"
        ordering = ("descr",)

    def save(self, *args, **kwargs):
        storage, path, id = self.image.storage, self.image.path, self.id
        try:
            v = Image.objects.get(id=id)
            storage.delete(v.image.name)
        except:
            pass
        super().save(*args, **kwargs)

    # only for file delete from folder
    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super().delete(*args, **kwargs)
        storage.delete(path)

# Product:- id#, item, descr, category (FK to Catagory)


class Product(m.Model):
    id = m.AutoField(primary_key=True)
    item = m.CharField(max_length=30, unique=True)
    descr = m.CharField(max_length=100)
    category = m.ForeignKey(Category, on_delete=m.RESTRICT)
    image = m.ForeignKey(Image, on_delete=m.RESTRICT)

    def __str__(self):
        return f"{self.item}"

    class Meta:
        db_table = "product"
        ordering = ("item",)

# Stock:- id#, product (FK to Product), price, quantity, mfg_date, exp_date, stock_date


class Stock(m.Model):
    id = m.AutoField(primary_key=True)
    product = m.ForeignKey(Product, on_delete=m.RESTRICT)
    price = m.DecimalField(max_digits=7, decimal_places=2)
    quantity = m.DecimalField(max_digits=7, decimal_places=2)
    stock_date = m.DateField()
    mfg_date = m.DateField()
    exp_date = m.DateField()

    def __str__(self):
        return f"{self.product.item}"

    class Meta:
        db_table = "stock"
        ordering = ("product",)

# Cart:- id#, stock (FK to Stock), user (FK to UserInfo)


class Cart(m.Model):
    id = m.AutoField(primary_key=True)
    stock = m.ForeignKey(Stock, on_delete=m.RESTRICT)
    user = m.ForeignKey(UserInfo, on_delete=m.RESTRICT)

    def __str__(self):
        return f"{self.stock} - {self.user}"

    class Meta:
        db_table = "cart"
        ordering = ("user", "user")

# Bill:- id#, bill_date, user (FK to UserInfo)


class Bill(m.Model):
    id = m.AutoField(primary_key=True)
    bill_date = m.DateField(auto_now_add=True, blank=True)
    user = m.ForeignKey(UserInfo, on_delete=m.RESTRICT)

    def __str__(self):
        return f"{self.bill_date} - {self.user}"

    class Meta:
        db_table = "bill"
        ordering = ("-bill_date",)

# PurchaseStatus:- #id, status


class PurchaseStatus(m.Model):
    id = m.AutoField(primary_key=True)
    status = m.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.status}"

    class Meta:
        db_table = "purchasestatus"

# Purchase:- id#, bill (FK to Bill), stock (FK to Stock), quantity, status (FK to PurchaseStatus)


class Purchase(m.Model):
    id = m.AutoField(primary_key=True)
    bill = m.ForeignKey(Bill, on_delete=m.RESTRICT)
    stock = m.ForeignKey(Stock, on_delete=m.RESTRICT)
    quantity = m.DecimalField(max_digits=7, decimal_places=2)
    status = m.ForeignKey(PurchaseStatus, on_delete=m.RESTRICT)

    def __str__(self):
        return f"{self.bill.bill_date} - {self.status}"

    @property
    def total(self):
        return round(self.stock.price * self.quantity, 2)

    class Meta:
        db_table = "purchase"
        ordering = ("-bill",)
