from django.db import models
from user.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator


class CoreModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


CITY_CHOICES = (
    ('Andijon', 'Andijon'),
    ('Namangan', 'Namangan'),
    ('Farg‘ona', 'Farg‘ona'),
    ('Toshkent', 'Toshkent'),
    ('Sirdaryo', 'Sirdaryo'),
    ('Jizzax', 'Jizzax'),
    ('Samarqand', 'Samarqand'),
    ('Qashqadaryo', 'Qashqadaryo'),
    ('Surxondaryo', 'Surxondaryo'),
    ('Buxoro', 'Buxoro'),
    ('Navoiy', 'Navoiy'),
    ('Xorazm', 'Xorazm'),
    ('Qoraqalpog‘iston', 'Qoraqalpog‘iston'),
)


class Category(CoreModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(CoreModel):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="product_image", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    piece = models.PositiveIntegerField(default=0, validators=[MinValueValidator(10), MaxValueValidator(100)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, choices=CITY_CHOICES)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}  -->  {self.user}'


class Comment(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    grade = models.FloatField(default=5, blank=True, null=True)

    def __str__(self):
        return f"{self.user}  -->  {self.product}"



