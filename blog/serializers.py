from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'

class PostDetailSerilizers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
