
from django.urls import path
from .views import MoviesView, MovieDetailView, AddReview, ActorView, AddStarRating, Search, video, CategoryView, genreview
from .filters import FilterMoviesView, JsonFilterView

urlpatterns = [
    path('', MoviesView.as_view(), name='base'),
    # path('series/', SeriesView.as_view(), name='series_list'),
    path('filter/', FilterMoviesView.as_view(), name = "filter"),
    path('search/', Search.as_view(), name = 'search'),
    path('genres/<str:url>/', genreview, name='genre_lists'),
    path('categories/<str:url>/', CategoryView, name = 'categories'),
    path('add-rating/', AddStarRating.as_view(), name = 'add_rating'),
    path('json-filter/', JsonFilterView.as_view(), name = 'json_filter'),
    path('<str:slug>/', MovieDetailView.as_view(), name = 'movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name = 'add_review'),
    path('actor/<str:slug>/', ActorView.as_view(), name = 'actor_detail'),

    
    
    path('video/', video, name = 'videos')
    

]