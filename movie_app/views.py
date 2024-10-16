from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import View
from movie_app.models import Movie, Genre
from movie_app.services import fetch_values_for_filters, generate_filters
from movie_app.forms import MovieForm


class MovieListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        genres = Genre.objects.all()
        objects = Movie.objects.all()
        return render(
            request,
            template_name="movie_app/movie_list.html",
            context={"genres": genres, "objects": objects, "title": "Список фильмов"},
        )


class MovieListViewByQuery(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        genres = Genre.objects.all()
        query = request.GET.get("query")
        objects = None
        if query:
            objects = Movie.objects.filter(
                Q(description__icontains=query) | Q(name__icontains=query)
            )
        return render(
            request,
            template_name="movie_app/movie_list.html",
            context={"genres": genres, "objects": objects, "title": "Список фильмов"},
        )


class MovieListViewFilter(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        genres = Genre.objects.all()
        rates = {movie.rate for movie in Movie.objects.all()}
        years = {movie.release for movie in Movie.objects.all()}
        return render(
            request,
            template_name="movie_app/filter.html",
            context={
                "genres": genres,
                "rates": rates,
                "years": years,
                "title": "Фильтры",
            },
        )


class MovieListViewByFilter(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        genres = Genre.objects.all()
        values_for_filters = fetch_values_for_filters(request.GET.items())
        filters = generate_filters(values_for_filters)
        objects = Movie.objects.filter(filters)
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


class NewMovieView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            template_name="movie_app/new_movie.html",
            context={
                "genres": Genre.objects.all(),
                "form": MovieForm(),
                "title": "Новый товар",
            },
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            object = Movie.objects.create(**form.cleaned_data)
            object.save()
            return redirect(object.get_absolute_url())
        return redirect(
            "movie:new-item",
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
