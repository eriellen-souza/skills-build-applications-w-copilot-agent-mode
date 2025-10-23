from django.urls import path
from django.http import HttpResponse


def health(request):
    return HttpResponse('OK')


urlpatterns = [
    path('', health, name='health'),
]
