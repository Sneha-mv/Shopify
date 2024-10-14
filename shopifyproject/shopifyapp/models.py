from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shopifyapp:category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

    
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('shopifyapp:proDetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
    

class Shopify(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    cpassword=models.CharField(max_length=30)
    
    def __str__(self):  
        return self.username


class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added = models.DateField(default=timezone.now)

    class Meta:
        db_table='Cart'
        ordering=['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        # Automatically update total amount on save
        self.total_amount = self.sub_total()
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name




    

