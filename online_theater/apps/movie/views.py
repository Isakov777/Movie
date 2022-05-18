


from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Actor, Category,  Movie, Genre_movie, Genre_series, Rating, Series, Cartoon, Anime, Genre_cartoon, Genre_anime, AllData, MovieVideo
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm, RatingForm, SeriesReviewForm, CartoonReviewForm, AnimeReviewForm
from.models import Item

from django.shortcuts import render


class GenreYear:
    def get_movies_genres(self):
        return Genre_movie.objects.all()
    def get_series_genres(self):
        return Genre_series.objects.all()
    def get_cartoon_genres(self):
        return Genre_cartoon.objects.all()
    def get_anime_genres(self):
        return Genre_anime.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft = False).values("year")




class AllDataViews(ListView):
    queryset = AllData.objects.all()
    context_object_name = 'all_data'
    template_name = 'all/list.html'



#--------------------------------------------------------------------------------------------------------------------------------------------------------
class MoviesView(GenreYear, ListView):
    
    model =  Movie
    queryset = Movie.objects.filter(draft = False)
    paginate_by = 3
    
    
def movie_genre_view(request, url):
    genre_movie = Movie.objects.filter(genres__url = url)
    return render(request, 'genres/index.html', {"genre_movie": genre_movie})


class MovieDetailView(GenreYear, DetailView):

    queryset = Movie.objects.all()

    slug_field = 'url'
    context_object_name = 'movie'
    template_name = 'movie/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['movie_videos'] = MovieVideo.objects.all()
        return context





#----------------------------------------------------------------------------------------------------------------------------------------
class SeriesView(GenreYear, ListView):
    
    model =  Series
    queryset = Series.objects.all()
    template_name = 'series/series_list.html'
    context_object_name = 'series_list'


def series_genre_view(request, url):
    genre_series = Series.objects.filter(genres__url = url)
    return render(request, 'series/index_genre.html', {"genre_series": genre_series})



class SeriesDetailView(GenreYear, DetailView):

    queryset = Series.objects.all()
    model = Series
    slug_field = 'url'
    context_object_name = 'series'
    template_name = 'series/series_detail.html'

    







#------------------------------------------------------------------------------------------------------------------------------------------------------------
class CartoonView(GenreYear, ListView):
    
    model =  Cartoon
    queryset = Cartoon.objects.all()
    template_name = 'cartoon/cartoon_list.html'
    context_object_name = 'cartoon_list'


def cartoon_genre_view(request, url):
    genre_cartoon = Cartoon.objects.filter(genres__url = url)
    return render(request, 'cartoon/index.html', {"genre_cartoon": genre_cartoon})


class CartoonDetailView(GenreYear, DetailView):

    queryset = Cartoon.objects.all()

    slug_field = 'url'
    context_object_name = 'cartoon'
    template_name = 'cartoon/cartoon_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context






#-----------------------------------------------------------------------------------------------------------------------------------------
class AnimeView(GenreYear, ListView):
    
    model =  Anime
    queryset = Anime.objects.all()
    template_name = 'anime/anime_list.html'
    context_object_name = 'anime_list'


def anime_genre_view(request, url):
    genre_anime = Anime.objects.filter(genres__url = url)
    return render(request, 'anime/anime_index.html', {"genre_anime": genre_anime})


class AnimeDetailView(GenreYear, DetailView):

    queryset = Anime.objects.all()

    slug_field = 'url'
    context_object_name = 'anime_detail'
    template_name = 'anime/anime_detail.html'

    



#---------------------------------------------------------------------------------------------------------------------------------------------------------------
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

class SeriesAddReview(View):

    def post(self, request, pk):
        series_form = SeriesReviewForm(request.POST)
        series_id = Series.objects.get(id = pk)
        if series_form.is_valid():
            series_form = series_form.save(commit=False)
            if request.POST.get("parent", None):
                series_form.parent_id = int(request.POST.get("parent"))
            series_form.series = series_id
            series_form.save()
        return redirect(series_id.get_absolute_url_series())



class CartoonAddReview(View):

    def post(self, request, pk):
        cartoon_form = CartoonReviewForm(request.POST)
        cartoon_id = Cartoon.objects.get(id = pk)
        if cartoon_form.is_valid():
            cartoon_form = cartoon_form.save(commit=False)
            if request.POST.get("parent", None):
                cartoon_form.parent_id = int(request.POST.get("parent"))
            cartoon_form.cartoon = cartoon_id
            cartoon_form.save()
        return redirect(cartoon_id.get_absolute_url_cartoon())



class AnimeAddReview(View):

    def post(self, request, pk):
        anime_form = AnimeReviewForm(request.POST)
        anime_id = Anime.objects.get(id = pk)
        if anime_form.is_valid():
            anime_form = anime_form.save(commit=False)
            if request.POST.get("parent", None):
                anime_form.parent_id = int(request.POST.get("parent"))
            anime_form.anime = anime_id
            anime_form.save()
        return redirect(anime_id.get_absolute_url_anime())


    
#-------------------------------------------------------------------------------------------------------------------------------------
class ActorView(GenreYear, DetailView):

    model = Actor
    template_name = 'movie/actor.html'
    slug_field = "name"





#----------------------------------------------------------------------------------------------------------------------------------------
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




#----------------------------------------------------------------------------------------------------------------------------------------
class MovieSearch(ListView):

    paginate_by = 3
    
    def get_queryset(self):
        return Movie.objects.filter(title__icontains = self.request.GET.get("key_word"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key_word"] = self.request.GET.get("key_word")

        return context




class SeriesSearch(ListView):

    paginate_by = 3
    template_name = 'series/series_list.html'
    
    def get_queryset(self):
        return Series.objects.filter(title__icontains = self.request.GET.get("key_word"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key_word"] = self.request.GET.get("key_word")

        return context




class CartoonSearch(ListView):

    paginate_by = 3
    template_name = 'cartoon/cartoon_list.html'
    
    def get_queryset(self):
        return Cartoon.objects.filter(title__icontains = self.request.GET.get("key_word"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key_word"] = self.request.GET.get("key_word")

        return context




class AnimeSearch(ListView):

    paginate_by = 3
    template_name = 'anime/anime_list.html'
    
    def get_queryset(self):
        return Anime.objects.filter(title__icontains = self.request.GET.get("key_word"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["key_word"] = self.request.GET.get("key_word")

        return context
#------------------------------------------------------------------------------------------------------------------



def all(request):
    movie = Movie.objects.all()
    series = Series.objects.all()
    cartoons = Cartoon.objects.all()
    anime = Anime.objects.all()
    content = {'movie':movie,
                'series':series,
                'cartoons':cartoons,
                'anime':anime}
    return render(request, 'all/all_data.html', content)