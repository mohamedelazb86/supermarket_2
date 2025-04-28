from . import serializers
from rest_framework import generics
from .models import Post

class PostApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostDetailSerilizers

    