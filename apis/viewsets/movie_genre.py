from rest_framework import mixins, viewsets
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from movie_app.models import Movie
from ..serializers.movie_genre import MovieSerializer, MovieDataSerializer


class MovieCreateListRetrieveViewSet(mixins.CreateModelMixin,
                                     mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.DestroyModelMixin,
                                     viewsets.GenericViewSet):
    permission_classes = []
    serializer_class = MovieDataSerializer
    queryset = Movie.objects.prefetch_related('genre').all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "director", "genre__title"]

    def get_permissions(self):
        if not (self.action == "list" or self.action == "retrieve"):
            return [IsAdminUser()]
        return self.permission_classes

    def get_serializer_class(self):
        if not (self.action == "list" or self.action == "retrieve"):
            return MovieSerializer
        return self.serializer_class
