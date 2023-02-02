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


# Create your views here.
class TeamView(APIView):
    def post(self, req: Request):
        try:
            data_processing(**req.data)
        except (ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError) as err:
            return Response({"Error": err.message}, 400)

        new_team = Team.objects.create(**req.data)

        new_team_dict = model_to_dict(new_team)

        return Response(new_team_dict, 201)
