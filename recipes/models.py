from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    origin = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)


def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(slug_pre_save, sender=Tag)
