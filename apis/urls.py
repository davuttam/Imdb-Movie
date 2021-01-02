from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.viewsets import movie_genre

router = DefaultRouter()

router.register(
    r'movie',
    movie_genre.MovieCreateListRetrieveViewSet,
    basename='movie'
)

urlpatterns = [
    path('', include(router.urls)),
]
