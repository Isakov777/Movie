
from statistics import mode
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




class Genre_movie(models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    url = models.SlugField(max_length=255, unique = True)

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Movie genre'
        verbose_name_plural = 'Movie genres'

    


class MovieVideo(models.Model):

    video = models.FileField(upload_to='movies/video/%y')








class Movie(models.Model):

    title = models.CharField(max_length = 255)
    tagline = models.CharField('Слоган', max_length = 255, ) 
    description = models.TextField()
    poster = models.ImageField(upload_to = 'movies/')
    year = models.PositiveIntegerField('дата выхода', default = 2022)
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(Actor, verbose_name='режисёр', related_name = 'movie_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='movie_actor')
    genres = models.ManyToManyField(Genre_movie, verbose_name = 'жанры', related_name='get_movie_genres')
    world_premier = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default = 0, help_text = 'указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('сборы в мире', default=0, help_text='указать сумму в долларах')
    videos = models.OneToOneField(MovieVideo, on_delete=models.CASCADE, related_name='movie_videos')
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





    





    
class Genre_series(models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    url = models.SlugField(max_length=255, unique = True)

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Series genre'
        verbose_name_plural = 'Series genres'

class SeriesVideo(models.Model):

    video = models.FileField(upload_to='series/video/%y')




class Series(models.Model):

    title = models.CharField(max_length = 255)
    genres = models.ManyToManyField(Genre_series, verbose_name = 'жанры', related_name='get_series_genres')
    tagline = models.CharField('Слоган', max_length = 255, ) 
    description = models.TextField()
    poster = models.ImageField(upload_to = 'movies/')
    year = models.PositiveIntegerField('дата выхода', default = 2022)
    country = models.CharField(max_length=255)
    world_premier = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default = 0, help_text = 'указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('сборы в мире', default=0, help_text='указать сумму в долларах')
    videos = models.OneToOneField(SeriesVideo, on_delete=models.CASCADE, related_name='series_videos')
    url = models.SlugField(max_length=255, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self) -> str:
        return self.title

    def get_series_review(self):
        return self.reviews_set_series.filter(parent__isnull = True)
    
    def get_absolute_url_series(self):
        return reverse('series_detail', kwargs = {'slug': self.url})




class Genre_cartoon(models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    url = models.SlugField(max_length=255, unique = True)

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Cartoon genre'
        verbose_name_plural = 'Cartoon genres'


class CartoonVideo(models.Model):

    video = models.FileField(upload_to='cartoon/video/%y')


class Cartoon(models.Model):

    title = models.CharField(max_length = 255)
    genres = models.ManyToManyField(Genre_cartoon, verbose_name = 'жанры', related_name='get_cartoon_genres')
    tagline = models.CharField('Слоган', max_length = 255, ) 
    description = models.TextField()
    poster = models.ImageField(upload_to = 'movies/')
    year = models.PositiveIntegerField('дата выхода', default = 2022)
    country = models.CharField(max_length=255)
    url = models.SlugField(max_length=255, unique=True)
    world_premier = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default = 0, help_text = 'указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('сборы в мире', default=0, help_text='указать сумму в долларах')
    videos = models.OneToOneField(CartoonVideo, on_delete=models.CASCADE, related_name='movie_videos')
    draft = models.BooleanField('Черновик', default=False)


    def __str__(self) -> str:
        return self.title


    def get_cartoon_review(self):
        return self.reviews_set_cartoon.filter(parent__isnull = True)

    def get_absolute_url_cartoon(self):
        return reverse('cartoon_detail', kwargs = {'slug': self.url})

 

class Genre_anime(models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    url = models.SlugField(max_length=255, unique = True)
    

    def __str__(self):
        return self.title

    

    class Meta:
        verbose_name = 'Anime genre'
        verbose_name_plural = 'Anime genres'


class AnimeVideo(models.Model):

    video = models.FileField(upload_to='video/%y')

class Anime(models.Model):

    title = models.CharField(max_length = 255)
    genres = models.ManyToManyField(Genre_anime, verbose_name = 'жанры', related_name='get_anime_genres')
    url = models.SlugField(max_length=255, unique=True)
    tagline = models.CharField('Слоган', max_length = 255, ) 
    description = models.TextField()
    poster = models.ImageField(upload_to = 'movies/')
    year = models.PositiveIntegerField('дата выхода', default = 2022)
    country = models.CharField(max_length=255)
    world_premier = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default = 0, help_text = 'указать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='указать сумму в долларах')
    fees_in_world = models.PositiveIntegerField('сборы в мире', default=0, help_text='указать сумму в долларах')
    videos = models.OneToOneField(AnimeVideo, on_delete=models.CASCADE, related_name='movie_videos')
    draft = models.BooleanField('Черновик', default=False)
    
    def __str__(self) -> str:
        return self.title

    def get_ainme_review(self):
        return self.reviews_set_anime.filter(parent__isnull = True)

    def get_absolute_url_anime(self):
        return reverse('anime_detail', kwargs = {'slug': self.url})



class AllData(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
 


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



class SeriesReview(models.Model):
    
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField("Отзыв" ,max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Подотзыв', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments_series_comment',)
    series = models.ForeignKey(Series, verbose_name='сериал', on_delete=models.CASCADE, related_name='reviews_set_series')


    def __str__(self) -> str:
        return f'{self.name} |---| {self.series}'



class CartoonReview(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField("Отзыв" ,max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Подотзыв', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments_cartoon_comment',)
    cartoon = models.ForeignKey(Cartoon, verbose_name='мультфильм', on_delete=models.CASCADE, related_name='reviews_set_cartoon')

    def __str__(self) -> str:
        return f'{self.name} |---| {self.cartoon}'

    

class AnimeReiview(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField("Отзыв" ,max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Подотзыв', on_delete=models.SET_NULL, blank=True, null=True, related_name='comments_anime_comment',)
    anime = models.ForeignKey(Anime, verbose_name='аниме', on_delete=models.CASCADE, related_name='reviews_set_anime')

    def __str__(self) -> str:
        return f'{self.name} |---| {self.cartoon}'






    
        




class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()