from collections import defaultdict

from app.birthdays.services import get_birthdays_per_week


def birthday_controller(users: list):
    birthday_map = defaultdict(list)

    if not len(users):
        return {}

    return get_birthdays_per_week(users, birthday_map)
