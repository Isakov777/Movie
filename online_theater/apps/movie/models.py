
from django.db import models
from datetime import date
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    title = models.CharField('Категория',max_length=255,)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


   





class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField('Age', default=0)
    descrption = models.TextField('descrption')
    image = models.ImageField(upload_to = 'actors/')
    url = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'




class Genre(models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    url = models.SlugField(max_length=255, unique = True)

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    

class Series(models.Model):
    title = models.CharField('Категория',max_length=255,)
    description = models.TextField('Описание')
    genres = models.ManyToManyField(Genre, verbose_name = 'жанры', related_name='get_series_genres')
    url = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Movie(models.Model):

    title = models.CharField(max_length = 255)
    tagline = models.CharField('Слоган', max_length = 255, ) 
    description = models.TextField()
    poster = models.ImageField(upload_to = 'movies/')
    year = models.PositiveIntegerField('дата выхода', default = 2022)
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(Actor, verbose_name='режисёр', related_name = 'movie_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='movie_actor')
    genres = models.ManyToManyField(Genre, verbose_name = 'жанры', related_name='get_movie_genres')
    world_premier = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default = 0, help_text = 'указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('сборы в мире', default=0, help_text='указать сумму в долларах')
    series = models.ForeignKey(Series, verbose_name='series', on_delete=models.SET_NULL, null=True, related_name='get_series')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True, related_name='get_categories')
    url = models.SlugField(max_length=255, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs = {'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull = True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'









    





# class Series(models.Model):

#     title = models.CharField(max_length = 255)
#     genres = models.ManyToManyField(Genre, verbose_name = 'жанры', related_name='get_series_genres')
#     category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, related_name='get_series_categories')
#     url = models.SlugField(max_length=255, unique=True)

#     def __str__(self) -> str:
#         return self.title









 


class MovieShots(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'movie_shots')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title 

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'



class RatingStar(models.Model):
    value = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ["-value"]




class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='фильм')

    def __str__(self) -> str:
        return f'Рейтинг: {self.movie} - {self.star} '

    class Meta:
        verbose_name = ' рейтинг'
        verbose_name_plural = 'рейтинги'
    



class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField("Отзыв" ,max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Подотзыв', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments_comment',)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE, related_name='reviews_set')

    def __str__(self) -> str:
        return f'{self.name} |---| {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        




class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()