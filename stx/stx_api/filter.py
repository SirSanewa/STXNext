import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name="authors__fullname", lookup_expr="icontains")

    from_date = django_filters.NumberFilter(field_name="published_year", lookup_expr="gte")
    to_date = django_filters.NumberFilter(field_name="published_year", lookup_expr="lte")

    acquired = django_filters.BooleanFilter(field_name="acquired")

    class Meta:
        model = Book
        fields = [
            "author",
            "from_date",
            "to_date",
            "acquired"
        ]
