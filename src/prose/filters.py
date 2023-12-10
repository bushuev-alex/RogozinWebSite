from django_filters import FilterSet
from prose.models import ProjitoeNeUgasaet


class ProseFilter(FilterSet):

    class Meta:
        model = ProjitoeNeUgasaet
        fields = {'id': ['exact']
                  }
