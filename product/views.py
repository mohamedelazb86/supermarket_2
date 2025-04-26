from django.shortcuts import render
from django.views.generic import ListView,DetailView
from product.models import Product,Brand


class Product_List(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by=12

class Product_Detail(DetailView):
    model=Product
    template_name='product/product_detail.html'
