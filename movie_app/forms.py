from django import forms
from movie_app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "name",
            "description",
            "genre",
            "cover",
            "release",
            "rate",
        ]
