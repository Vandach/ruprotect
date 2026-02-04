from django_distill import distill_path
from .views import index

urlpatterns = [
    distill_path(
        '',
        index,
        name='index',
        distill_file='index.html'
    ),
]