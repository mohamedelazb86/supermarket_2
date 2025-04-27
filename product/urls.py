from django.urls import path
from . import views


app_name='product'

urlpatterns = [
    # brand
    path('brands',views.Brand_List.as_view(),name='brand-list'),
    path('brand/<slug:slug>',views.Brand_Detail.as_view(),name='brand-detail'),


    #product
    path('',views.Product_List.as_view(),name='product-list'),
    path('<slug:slug>',views.Product_Detail.as_view(),name='product-detail'),
]
