from django.shortcuts import render
from apps.settings.models import Setting, About
from apps.secondary.models import Slider, Service, Team
from apps.products.models import Product, Category
# Create your views here.

def index(request):
    setting = Setting.objects.latest('id')
    slider = Slider.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    product_trand =  Product.objects.all()[:6]
    return render(request, 'base/index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    slider = Slider.objects.all()
    service = Service.objects.latest('id')
    about = About.objects.latest('id')
    team = Team.objects.all()
    return render(request, 'base/about.html', locals())