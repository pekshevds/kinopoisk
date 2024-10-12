from django.utils.safestring import mark_safe
from django.contrib import admin
from movie_app.models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ("name",)
    list_display = (
        "name",
        "id",
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "genre",
        "cover",
        "release",
        "rate",
        "description",
    )
    list_display = (
        "name",
        "genre",
        "preview",
        "release",
        "rate",
        "id",
    )
    list_filter = ("genre",)

    def preview(self, obj: Movie) -> str:
        str = ""
        if obj.cover:
            str = f'<img src="{obj.cover.url}"  style="max-height: 75px;">'
        return mark_safe(str)

    preview.short_description = "Обложка"
