# Generated by Django 4.1.1 on 2022-11-16 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_remove_gamemodel_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmodel',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.gamemodel'),
        ),
    ]
