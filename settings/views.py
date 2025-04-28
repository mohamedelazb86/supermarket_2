from django.shortcuts import render
from product.models import Product,Brand,Reviews
from django.db.models import Count

def home(request):
    brands=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))
    sale_product=Product.objects.filter(flag='Sale')[:10]
    new_product=Product.objects.filter(flag='New')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]
    top_product=Product.objects.all().order_by('-price')[:10]
    reviews=Reviews.objects.all()

    context={
        'brands':brands,
        'sale_product':sale_product,
        'new_product':new_product,
        'feature_product':feature_product,
        'top_product':top_product,
        'reviews':reviews
    }
    return render(request,'settings/home.html',context)
