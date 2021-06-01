from django.db import models

# Create your models here.
class Customer(models.Model):
    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=25)
    Phone = models.IntegerField()
    pinCode = models.IntegerField()

class Product(models.Model):
    pName = models.CharField(max_length=50)
    unitPrice = models.DecimalField(max_digits=6,decimal_places=2)
    # product_pic = models.ImageField(upload_to='images/',blank=True)

class Order(models.Model):
    customer_Id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_Id  = models.ForeignKey(Product,on_delete=models.CASCADE)
    unit_Price  = models.DecimalField(max_digits=6,decimal_places=2)
    Quntity = models.IntegerField()
    total_Price = models.DecimalField(max_digits=10,decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True,blank=False)
