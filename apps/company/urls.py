from django.urls import path

from apps.company.views import StatCountApi


urlpatterns = [
    path('count/', StatCountApi.as_view()),
]