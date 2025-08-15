from django.shortcuts import render

def cartView(request):
    return render(request, 'store/cart.html')

# Create your views here.
