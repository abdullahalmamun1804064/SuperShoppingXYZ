from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator

STATE_CHOICE=(
    ('dhaka','Dhaka'),
    ('shylet','Shylet'),
    ('chittagong','Chittagong'),
    ('barishal','Barishal'),
    ('rangpur','Rangpur'),
    ('comilla','Comilla'),
    ('rajshaie','Rajshaie'),
    ('maymensing','Maymensing'),
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_LIST=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Ware'),
    ('BW','Bottom Ware')
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    categary=models.CharField(choices=CATEGORY_LIST,max_length=2)
    image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self) :
        return str(self.id)
    @property
    def item_cost(self):
        return self.quantity * self.product.discount_price


STATUS_CHOICE=(
    ('accepted','Accepted'),
    ('packed','Packed'),
    ('on the way','On The Way'),
    ('delivered','Delivered'),
    ('cancel','Cancel')
)

class Orderplaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICE,max_length=50,default='Pending')

    def __str__(self) :
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price




