from django.core.management.base import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Tag.objects.filter(name='Acompanhamentos'):
            Tag.objects.create(name='Acompanhamentos')
        if not Tag.objects.filter(name='Tortas'):
            Tag.objects.create(name='Tortas')
        if not Tag.objects.filter(name='Bolos'):
            Tag.objects.create(name='Bolos')
        if not Tag.objects.filter(name='Aves'):
            Tag.objects.create(name='Aves')
        if not Tag.objects.filter(name='Bebidas'):
            Tag.objects.create(name='Bebidas')
        if not Tag.objects.filter(name='Carnes'):
            Tag.objects.create(name='Carnes')
        if not Tag.objects.filter(name='Entradas'):
            Tag.objects.create(name='Entradas')
        if not Tag.objects.filter(name='Lanches'):
            Tag.objects.create(name='Lanches')
        if not Tag.objects.filter(name='Massas'):
            Tag.objects.create(name='Massas')
        if not Tag.objects.filter(name='Molhos'):
            Tag.objects.create(name='Molhos')
        if not Tag.objects.filter(name='Pães e Salgados'):
            Tag.objects.create(name='Pães e Salgados')
        if not Tag.objects.filter(name='Peixes e Frutos'):
            Tag.objects.create(name='Peixes e Frutos')
        if not Tag.objects.filter(name='Saladas'):
            Tag.objects.create(name='Saladas')
