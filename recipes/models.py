from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)
