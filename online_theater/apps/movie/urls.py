
from django.urls import path
from .views import CartoonAddReview, MovieDetailView, AddReview, ActorView, AddStarRating, MovieSearch, SeriesSearch, CartoonSearch, AnimeSearch, movie_genre_view, series_genre_view, SeriesView, CartoonView, AnimeView, cartoon_genre_view, anime_genre_view, SeriesDetailView, CartoonDetailView, AnimeDetailView, AllDataViews, all, SeriesAddReview, MoviesView, AnimeAddReview
from .filters import FilterMoviesView, JsonFilterView

urlpatterns = [
    path('', all, name='base'),
    path('movies/', MoviesView.as_view(), name='movies_list'),
    path('series/', SeriesView.as_view(), name='series_list'),
    path('cartoon/', CartoonView.as_view(), name='cartoon_list'),
    path('anime/', AnimeView.as_view(), name='anime_list'),
    path('all/', AllDataViews.as_view(), name = 'all_data_list'),
    path('filter/', FilterMoviesView.as_view(), name = "filter"),
    path('movie/search/', MovieSearch.as_view(), name = 'movie_search'),
    path('video/', all, name='video'),
    path('series/search/', SeriesSearch.as_view(), name = 'series_search'),
    path('cartoon/search/', CartoonSearch.as_view(), name = 'cartoon_search'),
    path('anime/search/', AnimeSearch.as_view(), name = 'anime_search'),
    path('movies/<str:url>/', movie_genre_view, name='movie_genre_lists'),
    path('series_genre/<str:url>/', series_genre_view, name='series_genre_ist'),
    path('cartoon_genre/<str:url>/', cartoon_genre_view, name='cartoon_genre_ist'),
    path('anime_genre/<str:url>/', anime_genre_view, name='anime_genre_ist'),
    path('add-rating/', AddStarRating.as_view(), name = 'add_rating'),
    path('json-filter/', JsonFilterView.as_view(), name = 'json_filter'),
    path('<str:slug>/', MovieDetailView.as_view(), name = 'movie_detail'),
    path('series/<str:slug>/', SeriesDetailView.as_view(), name = 'series_detail'),
    path('cartoon/<str:slug>/', CartoonDetailView.as_view(), name = 'cartoon_detail'),
    path('anime/<str:slug>/', AnimeDetailView.as_view(), name = 'anime_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name = 'add_review'),
    path('series-review/<int:pk>/', SeriesAddReview.as_view(), name = 'series_add_review'),
    path('cartoon-review/<int:pk>/', CartoonAddReview.as_view(), name = 'cartoon_add_review'),
    path('cartoon-review/<int:pk>/', AnimeAddReview.as_view(), name = 'anime_add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name = 'actor_detail'),

    
    

    

]