from app.utils.logger import logger


def print_birthdays(birthdays: dict[list[str]]) -> None:
    for weekday, users in birthdays.items():
        users = ", ".join(users)
        logger.info(f"{weekday}: {users}")
    print("\n")
