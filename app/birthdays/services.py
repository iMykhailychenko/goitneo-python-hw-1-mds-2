from datetime import date, datetime


def change_birthday_to_this_year(birthday: date, year: int) -> date:
    """Changes year to current year and handles leap years exceptions"""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, day=(birthday.day - 1))


def get_birthdays_per_week(
    users: list, birthday_map: dict[list[str]]
) -> dict[list[str]]:
    today = datetime.today().date()

    for user in users:
        birthday_this_year = change_birthday_to_this_year(user.birthday, today.year)

        if birthday_this_year > today:
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                user_age = today.year - user.birthday.year
                weekday_name = (
                    birthday_this_year.strftime("%A")
                    if birthday_this_year.weekday() < 5
                    else "Monday"
                )
                birthday_map[weekday_name].append(f"{user.name} - {user_age} years old")

    return birthday_map
