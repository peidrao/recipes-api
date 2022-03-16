import os
import uuid

from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

from authentication.models import User


def recipe_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/recipe/', filename)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    origin = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    ingredients = models.ManyToManyField(Ingredient, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipes_tags')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f'{self.id}-{self.title}'


def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(slug_pre_save, sender=Tag)
