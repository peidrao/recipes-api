from rest_framework import serializers
from .models import Recipe, Tag, Ingredient

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Ingredient
        fields = '__all__'
    

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


    def create(self, validated_data):
        
        return super().create(validated_data)
