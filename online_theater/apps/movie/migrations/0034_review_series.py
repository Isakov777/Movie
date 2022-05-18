# Generated by Django 4.0.2 on 2022-05-11 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0033_alter_series_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to='movie.series', verbose_name='сериалы'),
            preserve_default=False,
        ),
    ]