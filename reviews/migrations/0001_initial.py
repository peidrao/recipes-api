# Generated by Django 4.0.3 on 2022-03-22 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0008_alter_recipe_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Very Good'), (5, 'Great')], default=3)),
                ('comment', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipe_review', to='recipes.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'review_recipe',
            },
        ),
    ]
