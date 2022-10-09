# Generated by Django 4.1.1 on 2022-10-09 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.categorymodel', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.blogtagmodel', verbose_name='tags'),
        ),
    ]
