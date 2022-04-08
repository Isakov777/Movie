





from re import template
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Actor,  Movie, Genre, Rating, Series
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm, RatingForm
from.models import Item

from django.shortcuts import render


class GenreYear:
    def get_genress(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft = False).values("year")

class SeriesGenre:
    def get_genre(self, id):
        series_genre = Series.objects.filter(genres__id = id)
        return series_genre


class MoviesView(GenreYear, ListView):
    
    model =  Movie
    queryset = Movie.objects.filter(draft = False)
    paginate_by = 3
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Series.objects.all()
        context = super(MoviesView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


# def GenreSeries(title):
#     genre = Genre.objects.all()
#     series_genre = Series.objects.get(genres = genre)
#     return series_genre  

def CategoryView(request, url):
    category_movies = Movie.objects.filter(category__url = url)
    return render(request, 'categories/index.html', {'category_movies': category_movies})

def genreview(request, url):
    genre_movie = Movie.objects.filter(genres__url = url)
    return render(request, 'genres/index.html', {"genre_movie": genre_movie})

# def genre(request):
#     genres = Genre.objects.all()
#     context = {'genres': genres}
#     return render(request, 'series/series_list.html', context)

# def CategoryView(request, url):
#     category_movies = Movie.objects.filter(category__url = url)
#     return render(request, 'categories/index.html', {'category_movies': category_movies})


# class SeriesView(GenreYear, ListView):
    
#     model =  Series
#     queryset = Series.objects.all()
#     template_name = 'series/series_list.html'
#     context_object_name = 'series_list'

    
#     def get_context_data(self, *args, **kwargs):
#         category_menu = Category.objects.all()
#         context = super(SeriesView, self).get_context_data(*args, **kwargs)
#         context['category_menu'] = category_menu
#         return context


        
class MovieDetailView(GenreYear, DetailView):

    queryset = Movie.objects.all()

    slug_field = 'url'
    context_object_name = 'movie'
    template_name = 'movie/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context



class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie_id = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie_id
            form.save()
        return redirect(movie_id.get_absolute_url())



class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movie/actor.html'
    slug_field = "name"






class AddStarRating(View):
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_x_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip = self.get_client_ip(request),
                movie_id = int(request.POST.get('movie')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status = 201)
        else:
            return HttpResponse(status = 400)


class Search(ListView):

    paginate_by = 3
    
    def get_queryset(self):
        return Movie.objects.filter(title__icontains = self.request.GET.get("key_word"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key_word"] = self.request.GET.get("key_word")

        return context



# class ItemView(ListView):
#     queryset = Item.objects.all()
#     template_name = 'videos/video.html'
#     context_object_name = 'my_videos'

def video(request):
    obj = Item.objects.all()
    return render(request, 'videos/video.html', {"my_vidoes": obj})
