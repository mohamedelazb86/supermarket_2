from django.urls import path
from . import views


app_name='product'

urlpatterns = [
    path('',views.Product_List.as_view(),name='product-list'),
    path('<slug:slug>',views.Product_Detail.as_view(),name='product-detail'),
]
