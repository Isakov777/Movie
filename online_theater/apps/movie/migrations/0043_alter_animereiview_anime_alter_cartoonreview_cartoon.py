# Generated by Django 4.0.2 on 2022-05-15 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0042_alter_animereiview_anime_alter_cartoonreview_cartoon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animereiview',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_anime', to='movie.anime', verbose_name='аниме'),
        ),
        migrations.AlterField(
            model_name='cartoonreview',
            name='cartoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_cartoon', to='movie.cartoon', verbose_name='мультфильм'),
        ),
    ]
