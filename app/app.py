from app.birthdays.controller import birthday_controller
from app.birthdays.view import print_birthdays
from app.bot.controller import bot_controller
from app.utils.get_users_list import get_users_list
from app.utils.logger import logger
from app.utils.print_task_indicator import print_task_indicator


class App:
    def task1(self):
        print_task_indicator("First task")
        print_birthdays(birthday_controller(get_users_list()))
        return self

    def task2(self):
        contacts = {}
        print_task_indicator("Second task")

        while True:
            logger.info("\nEnter a command: ")
            user_input = input()

            result = bot_controller(user_input, contacts)
            if result is None:
                logger.error("\nGood bye!")
                break
            logger.warn(result)

        return self
