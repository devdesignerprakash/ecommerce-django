from django.urls import path
from .views import*


urlpatterns = [
    path('',cartView,name="cart")
]
