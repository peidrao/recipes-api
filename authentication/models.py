from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Gender(models.TextChoices):
        MAN = "MAN", "Man"
        WOMAN = "WOMAN", "Woman"

    gender = models.CharField(
        verbose_name='Gênero', max_length=50, choices=Gender.choices, blank=True, null=True)

    phone = models.CharField(verbose_name='Telefone',
                             max_length=14, unique=True, null=True, blank=True)

    birthday = models.DateField(
        verbose_name='Data de Nascimento', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-id"]
