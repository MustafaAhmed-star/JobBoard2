import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    salary = django_filters.NumberFilter()
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = {'image','published_at','slug','owner','description'}