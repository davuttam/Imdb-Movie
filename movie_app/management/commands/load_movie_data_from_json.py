import os
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from movie_app.models import Movie, Genre


class Command(BaseCommand):
    help = 'Importing the data to db reading from json file.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Script execution Starting."))
        json_file = os.path.join(settings.BASE_DIR, "imdb.json")

        with open(json_file, 'r') as f:
            datas = json.loads(f.read())

            dict_data = {}

            for data in datas:
                dict_data["name"] = data.get("name")
                dict_data["director"] = data.get("director")
                dict_data["popularity"] = data.get("99popularity")
                dict_data["imdb_score"] = data.get("imdb_score")

                movie, created = Movie.objects.get_or_create(**dict_data)

                genres = data.get("genre")

                for title in genres:
                    genre, created = Genre.objects.get_or_create(title=title)
                    movie.genre.add(genre)
                movie.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(datas)} data"))
