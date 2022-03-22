from django.db import models

from authentication.models import User
from recipes.models import Recipe

# Create your models here.

class ReviewRecipe(models.Model):
    class Rate(models.IntegerChoices):
        VERY_BAD = 1
        BAD = 2
        GOOD = 3
        VERY_GOOD = 4
        GREAT = 5


    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_review')
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING, related_name='recipe_review')
    
    rate = models.IntegerField(choices=Rate.choices, default=Rate.GOOD)
    comment = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'review_recipe'


