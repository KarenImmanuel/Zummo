from rest_framework import serializers
from .models import Categories, Product

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Categories
        fields='__all__'
