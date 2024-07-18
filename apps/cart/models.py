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
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'