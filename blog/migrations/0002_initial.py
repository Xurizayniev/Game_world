# Generated by Django 4.1.1 on 2022-10-27 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
