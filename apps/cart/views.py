from django.shortcuts import render,redirect,get_object_or_404
from apps.settings.models import Setting, About
from apps.secondary.models import Slider, Service, Team
from apps.products.models import Product, Category
from apps.cart.models import Cart
# Create your views here.

def cart(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all()
    categories = Category.objects.all()
    cart_items = Cart.objects.all()
    total_price = sum([cart_item.total for cart_item in cart_items])
    cart_items_count = cart_items.count()
    return render(request, 'cart/cart.html', locals())

def add_to_cart(request, product_id):
    product_item = get_object_or_404(Product, pk=product_id)

    cart_item, created = Cart.objects.get_or_create(
        title=product_item.title,
        price=product_item.price,
        image=product_item.image,
        color=product_item.color,
        size=product_item.size,
    )
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')