from django.shortcuts import render
from category.models import Category
from store.models import Product
from django.shortcuts import get_object_or_404

def storeView(request,category_slug=None):
    categories=None
    products=None
    if(category_slug!=None):
        categories= get_object_or_404(Category, slug=category_slug)
        products= Product.objects.all().filter(category=categories, is_available=True)
    else:
        products= Product.objects.all().filter(is_available=True)
    context={
        # "categories":categories,
        "products":products
    }
    return render(request, 'store/store.html',context)

def product_detail(request, category_slug, product_slug):
    try:
         product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
         
    except Exception as e:
        raise e
    context={
        'product':product
    }
    return render(request, 'store/product-detail.html', context)




# Create your views here.
