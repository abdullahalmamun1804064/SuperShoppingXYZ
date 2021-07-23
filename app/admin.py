from django.contrib import admin
from .models import (Customer,Orderplaced,Cart,Product)


@admin.register(Customer)
class Customer_admin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','description','brand','categary','image']

@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Orderplaced)
class Order_place(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','order_date','status']
