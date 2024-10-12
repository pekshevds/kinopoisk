from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from movie_app.models import Movie, Genre


class MovieListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        genres = Genre.objects.all()
        objects = Movie.objects.all()
        return render(
            request,
            template_name="movie_app/movie_list.html",
            context={"genres": genres, "objects": objects, "title": "Список фильмов"},
        )


class MovieListByGenreView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        genre = get_object_or_404(Genre, id=id)
        objects = Movie.objects.filter(genre=genre)
        genres = Genre.objects.all()
        return render(
            request,
            template_name="movie_app/movie_list.html",
            context={"genres": genres, "objects": objects, "title": "Список фильмов"},
        )


class MovieView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        object = get_object_or_404(Movie, id=id)
        genres = Genre.objects.all()
        return render(
            request,
            template_name="movie_app/movie.html",
            context={"genres": genres, "object": object, "title": object.name},
        )


class NewMovieView(View):
    pass
