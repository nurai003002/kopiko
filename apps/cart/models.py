from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Cart(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    COLOR_CHOICES = (
        ('WHITE', 'WHITE'),
        ('BLACK', 'BLACK'),
        ('GRAY', 'GRAY'),
        ('BROWN', 'BROWN'),
    )
    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL')
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    color = models.CharField(
        max_length=255,
        verbose_name='Цвета',
        choices=COLOR_CHOICES,
        blank=True, null=True
    )
    size = models.CharField(
        max_length=100, verbose_name="Размер товара",
        choices=SIZE_CHOICES,
        default="S",
        blank=True, null=True
    )
    quantity = models.PositiveIntegerField(
        verbose_name = 'Количество продукта',
        blank=True, null=True
    )
    total = models.PositiveBigIntegerField(
        default=0, 
        verbose_name="Итоговая цена товаров")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'