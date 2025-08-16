import uuid
from django.db import models
from store.models import Product



# Create your models here.

class Cart(models.Model):
    cart_id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity=models.PositiveSmallIntegerField(default=1)
    is_active=models.BooleanField(default=True)

    class Meta:
        unique_together = ('cart', 'product')
    
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"

           

    

    
