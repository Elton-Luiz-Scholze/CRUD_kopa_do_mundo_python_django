from datetime import datetime


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def data_processing(**kwargs):
    first_world_cup = 1930
    actual_year = datetime.now()
    all_cups = []
    titles = kwargs["titles"]
    first_participations_in_cup = int(kwargs["first_cup"][0:4])
    possible_participations_in_cup = []

    for year in range(first_world_cup, actual_year.year, 4):
        all_cups.append(year)

    for year_cup in all_cups:
        if year_cup > first_participations_in_cup:
            possible_participations_in_cup.append(year_cup)

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if int(kwargs["first_cup"][0:4]) not in all_cups:
        raise InvalidYearCupError("there was no world cup this year")

    if titles > len(possible_participations_in_cup):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
