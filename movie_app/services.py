from typing import Any
from dataclasses import dataclass, field
from django.db.models import Q
from movie_app.models import Genre


@dataclass
class SelectedFilters:
    genres: set[Any] = field(default_factory=set)
    rates: set[int] = field(default_factory=set)
    years: set[int] = field(default_factory=set)


def fetch_value_from_key(key: str) -> str:
    return key.split("_")[1]


def fetch_values_for_filters(get: dict[str, Any]) -> SelectedFilters:
    sf = SelectedFilters()
    for key, _ in get:
        if "genre" in key:
            sf.genres.add(Genre.objects.get(id=fetch_value_from_key(key)))

        if "rate" in key:
            sf.rates.add(int(fetch_value_from_key(key)))

        if "year" in key:
            sf.years.add(int(fetch_value_from_key(key)))
    return sf


def generate_filters(sf: SelectedFilters) -> Q:
    filters = Q()
    if sf.genres:
        filters.add(Q(genre__in=sf.genres), Q.AND)
    if sf.rates:
        filters.add(Q(rate__in=sf.rates), Q.AND)
    if sf.years:
        filters.add(Q(release__in=sf.years), Q.AND)
    return filters
