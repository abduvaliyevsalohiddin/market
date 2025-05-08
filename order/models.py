from django.db import models
from main.models import CoreModel, Product
from user.models import Profile


class SelectedProduct(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} --> {self.product}"


class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    total_sum = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    summ = models.FloatField()
    amount = models.PositiveSmallIntegerField(default=1)

    # def save(self, *args, **kwargs):
    #     cart = Cart.objects.get(id=self.cart.id)
    #     price = self.product.price * self.amount
    #     cart.total_sum = price
    #     cart.save()
    #     super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.cart} --> {self.product} ---> {self.summ}"


class Order(CoreModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    summa = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.cart}"
