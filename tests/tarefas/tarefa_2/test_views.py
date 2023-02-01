from rest_framework.test import APITestCase
from teams.models import Team
from rest_framework.views import status


class CreateTeamTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/teams/"

    def test_if_a_team_can_be_created(self):
        team_data = {
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1930-07-13",
        }

        # REQUEST
        response = self.client.post(self.BASE_URL, data=team_data, format="json")

        # EXPECTED JSON RETURN
        expected_data = {
            "id": 1,
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1930-07-13",
        }
        result_data = response.json()
        msg = (
            "Verifique as informações da seleção retornada no POST "
            + f"em `{self.BASE_URL}` estão corretas."
        )
        self.assertEqual(expected_data, result_data, msg)

        # STATUS CODE
        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do POST "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_if_a_team_cannot_have_negative_titles(self):
        team_data = {
            "name": "Brasil",
            "titles": -5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1930-07-13",
        }

        # REQUEST
        response = self.client.post(self.BASE_URL, data=team_data, format="json")

        # EXPECTED JSON RETURN
        expected_data = {"error": "titles cannot be negative"}
        result_data = response.json()
        msg = (
            f"Verifique se a mensagem de erro retornada do POST em `{self.BASE_URL}` "
            + f"com `titles` negativo é `{expected_data}`"
        )
        self.assertEqual(expected_data, result_data, msg)

        # EXPECTED STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = (
            f"Verifique se o status code retornado do POST em `{self.BASE_URL}` "
            + f"com `titles` negativo é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_if_first_cup_is_a_valid_world_cup_year(self):
        team_data = {
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "2003-08-18",
        }

        # REQUEST
        response = self.client.post(self.BASE_URL, data=team_data, format="json")

        # EXPECTED JSON RETURN
        expected_data = {"error": "there was no world cup this year"}
        result_data = response.json()
        msg = (
            f"Verifique se a mensagem de erro retornada do POST em `{self.BASE_URL}` "
            + f"com `first_cup` nao sendo um ano de copa válido pós 1930 é `{expected_data}`"
        )
        self.assertEqual(expected_data, result_data, msg)

        # EXPECTED STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = (
            f"Verifique se o status code retornado do POST em `{self.BASE_URL}` "
            + f"com `first_cup` nao sendo um ano de copa válido pós 1930 é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_if_first_cup_cannot_be_before_1930(self):
        team_data = {
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1926-08-18",
        }

        # REQUEST
        response = self.client.post(self.BASE_URL, data=team_data, format="json")

        # EXPECTED JSON RETURN
        expected_data = {"error": "there was no world cup this year"}
        result_data = response.json()
        msg = (
            f"Verifique se a mensagem de erro retornada do POST em `{self.BASE_URL}` "
            + f"com `first_cup` anterior a 1930 é `{expected_data}`"
        )
        self.assertEqual(expected_data, result_data, msg)

        # EXPECTED STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = (
            f"Verifique se o status code retornado do POST em `{self.BASE_URL}` "
            + f"com `first_cup` anterior a 1930 é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)

    def test_if_title_number_is_possible_based_on_first_cup(self):
        team_data = {
            "name": "Brasil",
            "titles": 4,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "2022-08-18",
        }

        # REQUEST
        response = self.client.post(self.BASE_URL, data=team_data, format="json")

        # EXPECTED JSON RETURN
        expected_data = {"error": "impossible to have more titles than disputed cups"}
        result_data = response.json()
        msg = (
            f"Verifique se a mensagem de erro retornada do POST em `{self.BASE_URL}` "
            + f"com `titles` sendo impossivel baseado em `first_cup` é `{expected_data}`"
        )
        self.assertEqual(expected_data, result_data, msg)

        # EXPECTED STATUS CODE
        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code
        msg = (
            f"Verifique se o status code retornado do POST em `{self.BASE_URL}` "
            + f"com `titles` sendo impossivel baseado em `first_cup` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)


class ListTeamTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/teams/"

    def test_if_teams_can_be_listed(self):
        team_1_data = {
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1930-06-08",
        }
        team_2_data = {
            "name": "Argentina",
            "titles": 2,
            "top_scorer": "Lionel Messi",
            "fifa_code": "ARG",
            "first_cup": "1934-02-21",
        }

        # Criando time 1
        Team.objects.create(**team_1_data)
        # Criando time 2
        Team.objects.create(**team_2_data)

        # REQUEST
        response = self.client.get(self.BASE_URL)

        team_1_return = {**team_1_data, "id": 1}
        team_2_return = {**team_2_data, "id": 2}

        # EXPECTED JSON RETURN
        expected_data = [team_1_return, team_2_return]
        result_data = response.json()
        msg = (
            "Verifique se as informações das seleções listadas no GET "
            + f"em `{self.BASE_URL}` estão corretas."
        )
        self.assertEqual(expected_data, result_data, msg)

        # EXPECTED STATUS CODE
        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code
        msg = (
            "Verifique se o status code retornado do GET "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, result_status_code, msg)
