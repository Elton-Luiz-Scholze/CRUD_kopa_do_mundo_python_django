from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from .models import Team
from django.forms.models import model_to_dict
from .utils import (
    data_processing,
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)


class TeamView(APIView):
    def post(self, req: Request):
        try:
            data_processing(**req.data)
        except (ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError) as err:
            return Response({"error": err.message}, 400)

        new_team = Team.objects.create(**req.data)

        new_team_dict = model_to_dict(new_team)

        return Response(new_team_dict, 201)

    def get(self, req: Request):
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list)


class TeamInfoView(APIView):
    def get(self, req: Request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(team)

        return Response(team_dict, 200)
