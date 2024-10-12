from django.urls import path
from movie_app.views import index

app_name = "movie"
urlpatterns = [
    path("", index, name="index"),
]
