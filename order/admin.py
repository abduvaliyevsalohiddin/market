from django.contrib import admin
from .models import *

admin.site.register(SelectedProduct)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
