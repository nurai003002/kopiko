from django.shortcuts import render
from apps.settings.models import Setting, About
from apps.secondary.models import Slider, Service, Team
from apps.products.models import Product, Category
# Create your views here.

def cart(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'cart/cart.html', locals())