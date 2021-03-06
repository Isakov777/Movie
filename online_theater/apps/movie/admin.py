
from django.contrib import admin
from apps.movie.models import Genre_movie, Genre_series, Movie, MovieShots, Actor, RatingStar, Rating, Review, Series, Category, Cartoon, Genre_cartoon, Anime, Genre_anime, MovieVideo, SeriesVideo, CartoonVideo, AnimeVideo
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget 

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item, SeriesReview



class MovieAdminForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorUploadingWidget ())
    
    class Meta:
        model = Movie
        fields = '__all__'



# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "url", )
#     list_display_links = ['title']



class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',  'url', 'draft')
    list_filter = ( 'year',)
    search_fields = ('title', )
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft', )
    actions = ['published', 'unpublished']
    form = MovieAdminForm
    readonly_dields = ('get_image')
    # fields = (('actors', 'directors', 'geners'), )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline')),
        }),
        (None, {
            'fields': ('year', 'world_premier', 'country'),
        }),
        (None, {
            'fields': ('description', 'poster', 'videos')
        }),
        ("Actors", {
            'classes':('collapse'),
            'fields': (('actors', 'directors', 'genres', ), )
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'))
        }),
        (None, {
            'fields': (('url', 'draft'), )
        })
    )


    def unpublished(self, request, queryset):
        row_update = queryset.update(draft = True)
        if row_update == 1:
            message_bit = '1 ???????????? ???????? ??????????????????'
        else:
            message_bit = f'{row_update} ?????????????? ???????? ??????????????????'
        self.message_user(request, f'{message_bit}')

    def published(self, request, queryset):
        row_update = queryset.update(draft = False)
        if row_update == 1:
            message_bit = '1 ???????????? ???????? ??????????????????'
        else:
            message_bit = f'{row_update} ?????????????? ???????? ??????????????????'
        self.message_user(request, f'{message_bit}')

    published.short_description = '????????????????????????'
    published.allowed_permissions = ('change', )

    unpublished.short_description = '?????????? ?? ????????????????????'
    unpublished.allowed_permissions = ('change', )

    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')



admin.site.register(SeriesReview)


@admin.register(Genre_movie)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'id')

@admin.register(Genre_series)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'id')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image')
    readonlyfields = ('get_image')


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60"', )

    get_image.short_description = '??????????????????????'



@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'movie', "ip")


@admin.register(MovieShots)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('title', "movie")


# @admin.register(Category_movie)
# class Category_movieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'movie', 'description', 'url')



admin.site.register(RatingStar)


admin.site.register(Series)



class ItemAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category)   

admin.register(CartoonVideo)
class CartoonVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'id')


admin.site.register(Cartoon)


@admin.register(Genre_cartoon)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'id')

admin.site.register(Anime)

@admin.register(AnimeVideo)
class AnimeMovieAdmin(admin.ModelAdmin):
    list_display = ('video', 'id')

@admin.register(Genre_anime)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'id')

@admin.register(MovieVideo)
class MovieVideoAdmin(admin.ModelAdmin):
    list_display = ( 'video', 'id')

@admin.register(SeriesVideo)
class MovieVideoAdmin(admin.ModelAdmin):
    list_display = ( 'video', 'id')