from django.db import models
from main.models import CoreModel, Product
from user.models import Profile


class SelectedProduct(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} --> {self.product}"


class CartItem(CoreModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.profile.username} --> {self.product}"


class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS', 'IN_PROGRESS'
    COMPLETED = 'COMPLETED', 'COMPLETED'


class Order(CoreModel):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    address = models.TextField(blank=True, null=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    def __str__(self):
        return f"{self.profile}: {self.id}-order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.order.id}: {self.product.name}"


class Review(CoreModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.id}"
