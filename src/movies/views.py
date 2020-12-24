from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from movies import services
from movies.models import Movie, Actor
from movies.serializers import MovieListSerializer, MovieDetailSerializer, \
    ReviewCreateSerializer, SetMovieRatingSerializer, ActorsDetailSerializer, \
    ActorsListSerializer
from movies.services import MovieFilter


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка фильмов"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(
                                         ratings__ip=services.get_client_ip(
                                             self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(
                models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к фильму"""
    serializer_class = ReviewCreateSerializer


class SetMovieRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга фильму"""
    serializer_class = SetMovieRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=services.get_client_ip(self.request))


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод актеров или режиссеров"""
    queryset = Actor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorsListSerializer
        elif self.action == "retrieve":
            return ActorsDetailSerializer
