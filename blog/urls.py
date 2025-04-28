from django.urls import path
from . import views
from . import api


app_name='blog'

urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('update/<slug:slug>',views.update_post,name='update-post'),
    
    path('<slug:slug>',views.post_detail,name='post-detail'),
    path('delete/<slug:slug>',views.delete_post,name='delete-post'),

    # api
    path('posts/api',api.PostApi.as_view()),
    path('posts/api/<int:pk>',api.PostDetailApi.as_view()),
    
]
