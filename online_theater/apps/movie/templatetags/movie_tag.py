from django import template
from apps.movie.models import  Category, Movie, Series


register = template.Library()








@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()

# def get_series(id):

#     genres_s = Series.objects.get(id = id)
    
#     return 

@register.inclusion_tag('all/list.html')
def get_last_movies(count=5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}


# @register.inclusion_tag('all/list.html')
# def get_last_series(count=5):
#     series = Series.objects.order_by("id")[:count]
#     return {"last_series": series}

# @register.inclusion_tag('all/list.html')
# def get_all(*movies,):
#     return get_all(get_last_movies, get_last_series)