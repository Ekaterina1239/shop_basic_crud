from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    sale = models.PositiveIntegerField()
    cat_id = models.ForeignKey(Category,  on_delete=CASCADE)
    quantity = models.PositiveIntegerField()


class Cart(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()


class UserType(models.Model):
    type = models.CharField(max_length=255)


class User(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(UserType,  on_delete=CASCADE)
    password = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
