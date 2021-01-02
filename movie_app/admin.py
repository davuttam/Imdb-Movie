from django.contrib import admin

from .models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'imdb_score', 'director', 'popularity']
    list_filter = ['genre']
    search_fields = ['name', 'director']


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
