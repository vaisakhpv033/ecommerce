from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .models import cart, cartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def _cart_id(request):
    carts = request.session.session_key
    if not carts:
        carts = request.session.create()
    return carts


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        carts = cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        carts = cart.objects.create(cart_id=_cart_id(request))
        carts.save()
    try:
        cart_item = cartItem.objects.get(product=product, cart=carts)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except cartItem.DoesNotExist:
        cart_item = cartItem.objects.create(product=product, quantity=1, cart=carts)
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        carts = cart.objects.get(cart_id=_cart_id(request))
        cart_items = cartItem.objects.filter(cart=carts, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
    }
    return render(request, 'cart.html', context)


def cart_remove(request, product_id):
    carts = cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = cartItem.objects.get(product=product, cart=carts)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def full_remove(request, product_id):
    carts = cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = cartItem.objects.get(product=product, cart=carts)
    cart_item.delete()
    return redirect('cart:cart_detail')
