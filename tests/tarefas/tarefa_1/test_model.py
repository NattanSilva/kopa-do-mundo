from django.test import TestCase
from teams.models import Team


class TeamModelTest(TestCase):
    def test_name_properties(self):
        expected = 30
        result = Team._meta.get_field("name").max_length
        msg = f"Verifique se a propriedade `max_length` de `name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

    def test_titles_properties(self):
        result = Team._meta.get_field("titles").null
        msg = f"Verifique se o atributo `titles` foi definido como opcional"
        self.assertTrue(result, msg)

        result = Team._meta.get_field("titles").default
        expected = 0
        msg = f"Verifique se a propriedade `default` de `titles` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

    def test_top_scorer_properties(self):
        expected = 50
        result = Team._meta.get_field("top_scorer").max_length
        msg = f"Verifique se a propriedade `max_length` de `top_scorer` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

    def test_fifa_code_properties(self):
        expected = 3
        result = Team._meta.get_field("fifa_code").max_length
        msg = f"Verifique se a propriedade `max_length` de `fifa_code` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Team._meta.get_field("fifa_code").unique
        msg = f"Verifique se o atributo `fifa_code` foi definido como unico"
        self.assertTrue(result, msg)

    def test_first_cup_properties(self):
        result = Team._meta.get_field("first_cup").null
        msg = f"Verifique se o atributo `first_cup` foi definido como opcional"
        self.assertTrue(result, msg)

    def test_object_representation(self):
        team_1_data = {
            "name": "Brasil",
            "titles": 5,
            "top_scorer": "Pelé",
            "fifa_code": "BRA",
            "first_cup": "1914-06-08",
        }
        # Criando time 1
        team = Team.objects.create(**team_1_data)

        msg = "Verifique se a representação de objetos de Team está de acordo com o pedido"
        expected = "<[1] Brasil - BRA>"
        result = team.__repr__()
        self.assertEqual(expected, result, msg)
