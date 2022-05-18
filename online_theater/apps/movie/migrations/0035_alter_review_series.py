# Generated by Django 4.0.2 on 2022-05-11 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0034_review_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set_series', to='movie.series', verbose_name='сериалы'),
        ),
    ]