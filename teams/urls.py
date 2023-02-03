from django.urls import path
from .views import TeamInfoView, TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamInfoView.as_view()),
]
