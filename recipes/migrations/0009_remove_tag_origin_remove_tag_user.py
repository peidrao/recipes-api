# Generated by Django 4.0.3 on 2022-04-24 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
