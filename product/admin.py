from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Product_Image,Reviews,Brand


class ImageProduct(admin.TabularInline):
    model=Product_Image

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','price','quantity']
    search_fields=['name','subtitle','descriptions','slug']
    list_filter=['brand']
    summernote_fields=('subtitle','descriptions')


    inlines=[ImageProduct,]

admin.site.register(Product,ProductAdmin)

admin.site.register(Reviews)
admin.site.register(Brand)
