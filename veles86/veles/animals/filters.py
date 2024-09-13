from django_filters import FilterSet  # импортируем filterset
from .models import Dog


# создаём фильтр
class DogFilter(FilterSet):

     class Meta:
        model = Dog
        fields = {
            'name': ['icontains' ],
        }


