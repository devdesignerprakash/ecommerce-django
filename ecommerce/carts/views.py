from django.shortcuts import render,redirect
from store.models import Product
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import uuid

def _create_cart(request):
    cart= request.session.get('cart_id')
    if not cart:
        cart=str(uuid.uuid4())
        request.session['cart_id']=cart
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Get or create cart
    try:
        cart = Cart.objects.get(cart_id=_create_cart(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_create_cart(request))
        cart.save()
    
    # Get or create cart item
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    
    # Redirect after handling cart item
    return redirect('cart')  # make sure this URL name exists

def cartView(request, total=0, cart_items=None):
    try:
        cart_items= CartItem.objects.filter(cart__cart_id=_create_cart(request))
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
           
            # quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    context={
        'total':total,
        'cart_items':cart_items
    }
    return render(request, 'store/cart.html',context)

# Create your views here.
