# Generated by Django 4.1.1 on 2022-11-16 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0008_gamemodel_average_rating_ratingmodel_dislike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmodel',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.gamemodel'),
        ),
        migrations.AlterField(
            model_name='ratingmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
