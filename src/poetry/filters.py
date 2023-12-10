from django_filters import FilterSet
from django.forms import DateInput
from .models import ChildPoetry


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PoetryFilter(FilterSet):

    class Meta:
        model = ChildPoetry
        fields = {'title': ['exact']
                  }
