from .models import Movie, Genre_movie
from django.views.generic import ListView
from django.http import JsonResponse
from django.db.models import Q

class GenreYear:
    def get_genres(self):
        return Genre_movie.objects.all()


class FilterMoviesView(GenreYear, ListView):

    paginate_by = 3

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in = self.request.GET.getlist("year")) | 
            Q(genres__in = self.request.GET.getlist("genre")) |
            Q(title__in = self.request.GET.getlist("search"))
            ).distinct() 

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f'year={x}&' for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f'genre={x}&' for x in self.request.GET.getlist("genre")])
        return context

class JsonFilterView(ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in = self.request.GET.getlist("year")) |
            Q(genres__in = self.request.GET.getlist("genre"))
        ).distinct().values('title', 'tagline', 'url', 'poster')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({'movie': queryset}, safe = False)