from django.urls import path
from .views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
]