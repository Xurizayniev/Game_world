# Generated by Django 4.1.1 on 2022-10-14 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.gamecategorymodel', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.companymodel', verbose_name='company'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='platform',
            field=models.ManyToManyField(to='games.platformmodel', verbose_name='platform'),
        ),
    ]
