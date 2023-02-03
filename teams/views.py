from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import Team
from .utils import (ImpossibleTitlesError, InvalidYearCupError,
                    NegativeTitlesError, data_processing)


class TeamView(APIView):
    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        try:
            data_processing(req.data)
        except NegativeTitlesError as error:
            return Response(
                {"error": error.message},
                status.HTTP_400_BAD_REQUEST
            )
        except InvalidYearCupError as error:
            return Response(
                {"error": error.message},
                status.HTTP_400_BAD_REQUEST
            )
        except ImpossibleTitlesError as error:
            return Response(
                {"error": error.message},
                status.HTTP_400_BAD_REQUEST
            )

        team = Team.objects.create(**req.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, req: Request, team_id) -> Response:
        try:
            current_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist as error:
            return Response(
                {"message": "Team not found"},
                status.HTTP_404_NOT_FOUND
            )

        team_dict = model_to_dict(current_team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, req: Request, team_id) -> Response:
        try:
            current_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist as error:
            return Response(
                {"message": "Team not found"},
                status.HTTP_404_NOT_FOUND
            )

        current_team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, team_id) -> Response:
        try:
            current_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist as error:
            return Response(
                {"message": "Team not found"},
                status.HTTP_404_NOT_FOUND
            )

        for key, value in req.data.items():
            setattr(current_team, key, value)

        current_team.save()
        team_dict = model_to_dict(current_team)

        return Response(team_dict, status.HTTP_200_OK)
