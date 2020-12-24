from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = format_suffix_patterns([
    path('movies/', views.MovieViewSet.as_view({'get': 'list'})),
    path('movies/<int:pk>/', views.MovieViewSet.as_view({'get': 'retrieve'})),
    path('create-review/',
         views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path('set-movie-rating/',
         views.SetMovieRatingViewSet.as_view({'post': 'create'})),

    path('actors/', views.ActorsViewSet.as_view({'get': 'list'})),
    path('actors/<int:pk>/', views.ActorsViewSet.as_view({'get': 'retrieve'})),
])
