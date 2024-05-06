import uuid
from datetime import date
from time import timezone

from django.db import models
from django.template.defaultfilters import random


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


label_choice = {
    'по свету': 'по свету',
    'по цвету': 'по цвету',
    'по формату': 'по формату',
}


class Label(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, choices=label_choice)

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

    def __str__(self):
        return self.title


class Flower(models.Model):
    title = models.CharField(max_length=255)
    id_label = models.ForeignKey(Label, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'

    def __str__(self):
        return f'{self.title}'


status_order = [('В ожидании', 'В ожидании'), ('Доставлено', 'Доставлено')]


class Order(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=200, choices=status_order, default='В ожидании')
    comments = models.TextField(null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery = models.CharField(max_length=200, choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')])
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.phone_number} - {self.total}'


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='flower/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='product_categories')
    label = models.ManyToManyField(Label, related_name='product_labels')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Composition(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='composition_product')
    id_flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='composition')
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Состав букета'
        verbose_name_plural = 'Состав букетов'

    def __str__(self):
        return f'{self.id_product.title} - {self.id_flower.title}'


class Review(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=5)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('id_product', 'email')

    def __str__(self):
        return f'{self.id_product.title} - {self.rating} - {self.name}'


class OrderItem(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Состав заказа'
        verbose_name_plural = 'Состав заказов'
        index_together = ('id_order', 'id_product')

    def __str__(self):
        return f'{self.id_order.pk} - {self.id_product.title}'


class Application(models.Model):
    name_of_company = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_person_phone = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.EmailField()
    unp = models.CharField(max_length=255)
    checking_account = models.CharField(max_length=255)
    bank_code = models.CharField(max_length=255)
    applications_per_month = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки корпоративные'

    def __str__(self):
        return f'{self.name_of_company}'


class DeliveryAddress(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса'
