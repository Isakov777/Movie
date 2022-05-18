# Generated by Django 4.0.2 on 2022-05-15 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0041_cartoonreview_animereiview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animereiview',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_series', to='movie.anime', verbose_name='аниме'),
        ),
        migrations.AlterField(
            model_name='cartoonreview',
            name='cartoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_series', to='movie.cartoon', verbose_name='мультфильм'),
        ),
        migrations.AlterField(
            model_name='seriesreview',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_series', to='movie.series', verbose_name='сериал'),
        ),
    ]
