from django.urls import path
from movie_app.views import (
    MovieListView,
    MovieListViewByQuery,
    MovieView,
    NewMovieView,
    MovieListByGenreView,
    MovieListViewFilter,
    MovieListViewByFilter,
)

app_name = "movie"
urlpatterns = [
    path("", MovieListView.as_view(), name="list"),
    path("query-result/", MovieListViewByQuery.as_view(), name="by-query"),
    path("filter/", MovieListViewFilter.as_view(), name="filter"),
    path("filter-result/", MovieListViewByFilter.as_view(), name="by-filter"),
    path("movie/item/<str:id>/", MovieView.as_view(), name="item"),
    path("movie/new/", NewMovieView.as_view(), name="new-item"),
    path("genre/item/<str:id>/", MovieListByGenreView.as_view(), name="by-genre"),
]
