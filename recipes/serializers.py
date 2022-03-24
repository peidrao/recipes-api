from rest_framework import serializers

from reviews.models import ReviewRecipe
from .models import Recipe, Tag, Ingredient

from authentication.serializers import UserSerializer

class TagSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = "__all__"
    
    def create(self, validated_data):
        instance = super(TagSerializer, self).create(validated_data)
        instance.user = self.context['request'].user
        instance.save()
        return instance
    
    def get_user(self, obj):
        if obj.user:
            return dict(id=obj.id, username=obj.user.username, email=obj.user.email)
        return {}


class IngredientSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Ingredient
        fields = '__all__'

    def create(self, validated_data):
        instance = super(IngredientSerializer, self).create(validated_data)
        instance.user = self.context['request'].user
        instance.save()
        return instance
    

class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('title', 'price', 'time_minutes', 'ingredients', 'tags', 'image', 'user', 'reviews')

    def get_user(self, obj):
        if obj.user:
            return dict(id=obj.id, username=obj.user.username, email=obj.user.email)
        return {}

    def create(self, validated_data):
        instance = super(RecipeSerializer, self).create(validated_data)
        instance.user = self.context['request'].user
        instance.save()
        return instance

    def get_tags(self, obj):
        tags = obj.tags.all()
        json = []
        for tag in tags:
            i = {}
            i['name'] = tag.name
            i['slug'] = tag.slug
            json.append(i)
        
        return json

    def get_reviews(self, obj):
        reviews = ReviewRecipe.objects.filter(recipe_id=obj.id)
        
        json = []
        if reviews.exists():
            for i in reviews:
                review = {}
                review['id'] = i.id
                review['user'] = i.user.username
                review['rate'] = i.rate
                review['comment'] = i.comment
                json.append(review)

        return json