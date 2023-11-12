import unittest
from datetime import date
from unittest.mock import patch

from app.birthdays.controller import birthday_controller
from app.models import Birthday


class TestBirthdaysController(unittest.TestCase):
    mock_date = date(2023, 6, 6)  # mock date (Tuesday)

    def test_empty_list(self):
        """Returns empty dict if there is no birthdays"""
        actual = birthday_controller([])
        self.assertEqual(actual, {})

    @patch("app.birthdays.services.datetime")
    def test_two_valid_birthdays(self, mock_date):
        """Returns dict with two valid birthdays
        and skips all birthdays that is not in upcoming week"""

        mock_date.today.return_value.date.return_value = self.mock_date

        users = [
            Birthday(name="User1 User1", birthday=date(1998, 10, 20)),  # should skip
            Birthday(name="User2 User2", birthday=date(1995, 6, 7)),  # Wednesday
            Birthday(name="User3 User3", birthday=date(2000, 6, 9)),  # Friday
            Birthday(name="User4 User4", birthday=date(1992, 4, 16)),  # should skip
        ]

        expected = {
            "Wednesday": ["User2 User2 - 28 years old"],
            "Friday": ["User3 User3 - 23 years old"],
        }

        actual = birthday_controller(users)
        self.assertEqual(actual, expected)

    @patch("app.birthdays.services.datetime")
    def test_few_birthdays_in_one_day(self, mock_date):
        """Returns multiple birthdays in one day"""

        mock_date.today.return_value.date.return_value = self.mock_date

        users = [
            Birthday(name="User1 User1", birthday=date(1998, 10, 20)),  # should skip
            Birthday(name="User2 User2", birthday=date(1995, 6, 7)),  # Wednesday
            Birthday(name="User3 User3", birthday=date(2000, 6, 7)),  # Wednesday
            Birthday(name="User4 User4", birthday=date(1992, 4, 16)),  # should skip
            Birthday(name="User5 User5", birthday=date(1991, 6, 7)),  # Wednesday
        ]

        expected = {
            "Wednesday": [
                "User2 User2 - 28 years old",
                "User3 User3 - 23 years old",
                "User5 User5 - 32 years old",
            ],
        }

        actual = birthday_controller(users)
        self.assertEqual(actual, expected)

    @patch("app.birthdays.services.datetime")
    def test_leap_year(self, mock_date):
        """Handles leap years properly"""

        mock_date.today.return_value.date.return_value = self.mock_date

        users = [
            Birthday(name="User1 User1", birthday=date(1998, 10, 20)),  # should skip
            Birthday(
                name="User2 User2", birthday=date(1992, 6, 9)
            ),  # Leap year, Friday
            Birthday(
                name="User3 User3", birthday=date(1992, 6, 9)
            ),  # Leap year, Friday
            Birthday(name="User5 User5", birthday=date(1995, 6, 7)),  # Wednesday
        ]

        expected = {
            "Friday": [
                "User2 User2 - 31 years old",
                "User3 User3 - 31 years old",
            ],
            "Wednesday": ["User5 User5 - 28 years old"],
        }

        actual = birthday_controller(users)
        self.assertEqual(actual, expected)

    @patch("app.birthdays.services.datetime")
    def test_moves_weekends(self, mock_date):
        """Moves weekends days to next week"""

        mock_date.today.return_value.date.return_value = self.mock_date

        users = [
            Birthday(name="User1 User1", birthday=date(1998, 10, 20)),  # should skip
            Birthday(name="User2 User2", birthday=date(1993, 6, 10)),  # Saturday
            Birthday(name="User3 User3", birthday=date(1993, 6, 11)),  # Sunday
            Birthday(name="User5 User5", birthday=date(1995, 6, 7)),  # Wednesday
        ]

        expected = {
            "Monday": ["User2 User2 - 30 years old", "User3 User3 - 30 years old"],
            "Wednesday": ["User5 User5 - 28 years old"],
        }

        actual = birthday_controller(users)
        self.assertEqual(actual, expected)
