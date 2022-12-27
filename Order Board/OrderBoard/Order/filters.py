from django_filters import FilterSet
from .models import Comments


class CommentFilter(FilterSet):
    class Meta:
        model = Comments
        fields = {
            'commentOrder__title': ['icontains'],
        }
