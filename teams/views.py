from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import Team
from .utils import data_processing


class TeamView(APIView):
    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        data_test = data_processing(req.data)
        if data_test[0]:
            return Response(data_test[1], status.HTTP_400_BAD_REQUEST)
        else:
            team = Team.objects.create(**req.data)
            team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)
