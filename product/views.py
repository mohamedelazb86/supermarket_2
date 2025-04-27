from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from product.models import Product,Brand,Reviews,Product_Image
from django.db.models import Count


class Product_List(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by=12

class Product_Detail(DetailView):
    model=Product
    template_name='product/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Reviews.objects.filter(product=self.get_object()).order_by('-id')[:2]
        context["images"] = Product_Image.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        
        return context
    
def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    user=request.user
    review=request.POST['review']
    rate=request.POST['rating']

    Reviews.objects.create(
        user=user,
        product=product,
        review=review,
        rate=rate

    )
    return redirect(f'/product/{slug}')
    



class Brand_List(ListView):
    model=Brand
    template_name='product/brand_list.html'
    paginate_by=25

    queryset=Brand.objects.all().annotate(product_count=Count('product_brand'))
    

# class Brand_Detail(DetailView):
#     model=Brand
#     template_name='product/brand_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["products"] = Product.objects.filter(brand=self.get_object())
#         return context
    

class Brand_Detail(ListView):
    model=Product
    template_name='product/brand_detail.html'
    paginate_by=5

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=Product.objects.filter(brand=brand)
        return queryset
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    

  