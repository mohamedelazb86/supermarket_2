from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
]
class Product(models.Model):

    name=models.CharField(max_length=120)
    flag=models.CharField(max_length=35,choices=FLAG_TYPE)
    price=models.FloatField()
    image=models.ImageField(upload_to='photo_product')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=1500)
    descriptions=models.TextField(max_length=20000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    @property
    def review_count(self):
        reviews=self.product_review.all().count()

        return reviews
    
    @property
    def avg_rate(self):
        total=0
        reviews=self.product_review.all()
        if len(reviews) > 0:
            for item in reviews:
                total +=item.rate
            avg=total/len(reviews)
        else:
            avg=0
        return avg



class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='photo_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)
        

class Product_Image(models.Model):

    product=models.ForeignKey(Product,related_name='images_product',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)

class Reviews(models.Model):

    user=models.ForeignKey(User,related_name='review_user_product',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    review=models.TextField(max_length=750)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)

