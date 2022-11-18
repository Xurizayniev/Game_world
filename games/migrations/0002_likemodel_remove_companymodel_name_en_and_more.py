# Generated by Django 4.1.1 on 2022-11-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], max_length=10)),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='companymodel',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='platformmodel',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='platformmodel',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='platformmodel',
            name='name_uz',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='average_rating',
            field=models.FloatField(default=0.0, verbose_name='Average rating'),
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('rating', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.gamemodel')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
