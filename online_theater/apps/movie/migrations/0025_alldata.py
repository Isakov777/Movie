# Generated by Django 4.0.2 on 2022-04-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0024_alter_anime_genres_alter_cartoon_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.anime')),
                ('cartoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.cartoon')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.series')),
            ],
        ),
    ]
