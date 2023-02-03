class NegativeTitlesError(Exception):
    default_message = "titles cannot be negative"

    def __init__(self, message=None):
        self.message = message or self.default_message


class InvalidYearCupError(Exception):
    default_message = "there was no world cup this year"

    def __init__(self, message=None):
        self.message = message or self.default_message


class ImpossibleTitlesError(Exception):
    default_message = "impossible to have more titles than disputed cups"

    def __init__(self, message=None):
        self.message = message or self.default_message


def includes(lista: list, valor_buscado: int) -> bool:
    for value in lista:
        if value == valor_buscado:
            return True
    return False


def get_year_interval(start: int, end: int) -> int:
    cup_years = [
        1930, 1934, 1938, 1950, 1954,
        1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994,
        1998, 2002, 2006, 2010, 2014,
        2018, 2022
    ]
    result = []
    for value in cup_years:
        if value >= start and value <= end:
            result.append(value)
    return len(result)


def data_processing(dict_selection):
    first_cup_year = int(dict_selection["first_cup"][0:4])
    cup_years = [
        1930, 1934, 1938, 1950, 1954,
        1958, 1962, 1966, 1970, 1974,
        1978, 1982, 1986, 1990, 1994,
        1998, 2002, 2006, 2010, 2014,
        2018, 2022
    ]

    if dict_selection["titles"] < 0:
        raise NegativeTitlesError()

    if not includes(cup_years, first_cup_year):
        raise InvalidYearCupError()

    if int(dict_selection["titles"]) > get_year_interval(first_cup_year, 2022):
        raise ImpossibleTitlesError()

# data = {
#     "name": "França",
#     "titles": -3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "2000-10-18"
# }

# print(data_processing(data))


# data = {
#     "name": "França",
#     "titles": 3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "1911-10-18"
# }

# print(data_processing(data))
# InvalidYearCupError: there was no world cup this year

# data = {
#     "name": "França",
#     "titles": 3,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "1932-10-18"
# }

# print(data_processing(data))
# InvalidYearCupError: there was no world cup this year

# data = {
#     "name": "França",
#     "titles": 9,
#     "top_scorer": "Zidane",
#     "fifa_code": "FRA",
#     "first_cup": "2002-10-18",
# }

# print(data_processing(data))
# ImpossibleTitlesError: impossible to have more titles than disputed cups
