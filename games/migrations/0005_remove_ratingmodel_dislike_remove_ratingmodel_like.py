# Generated by Django 4.1.1 on 2022-11-16 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_ratingmodel_dislike_ratingmodel_like_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingmodel',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='ratingmodel',
            name='like',
        ),
    ]
