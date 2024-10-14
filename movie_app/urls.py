from django.urls import path
from movie_app.views import (
    MovieListView,
    MovieListViewByQuery,
    MovieView,
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
    path("movie/<str:id>/", MovieView.as_view(), name="item"),
    path("genre/<str:id>/", MovieListByGenreView.as_view(), name="by-genre"),
]
