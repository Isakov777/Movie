# Generated by Django 4.0.2 on 2022-04-09 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0020_remove_movie_series_remove_series_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.RemoveField(
            model_name='series',
            name='category',
        ),
    ]
