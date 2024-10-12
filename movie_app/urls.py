from django.urls import path
from movie_app.views import MovieListView, MovieView, MovieListByGenreView

app_name = "movie"
urlpatterns = [
    path("movie/", MovieListView.as_view(), name="list"),
    path("movie/<str:id>/", MovieView.as_view(), name="item"),
    path("genre/<str:id>/", MovieListByGenreView.as_view(), name="by-genre"),
]
