from django.db import models

from django.utils.text import slugify


class Genre(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Genre, self).save(*args, **kwargs)


class Movie(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=55)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    genre = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return self.name
