from rest_framework import serializers

from .models import ReviewRecipe


class ReviewRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewRecipe
        fields = '__all__'