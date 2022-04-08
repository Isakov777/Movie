from django import template
from apps.movie.models import Series, Genre, Category


register = template.Library()


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.simple_tag()
def get_series():
    so_series = Series.objects.all()
    return so_series


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()

# def get_series(id):

#     genres_s = Series.objects.get(id = id)
    
#     return 

# @register.inclusion_tag('movie/tags/last_movie.html')
# def get_last_movies(count=5):
#     movies = Movie.objects.order_by("id")[:count]
#     return {"last_movies": movies}
