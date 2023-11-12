import unittest

from app.bot.controller import bot_controller


class TestBotController(unittest.TestCase):
    def test_exit_command(self):
        """Returns None for exit or close commands"""
        result = bot_controller("exit", {})
        self.assertEqual(result, None)

        result = bot_controller("close", {})
        self.assertEqual(result, None)

    def test_case_insensitive(self):
        """Handle 'Hello' command in case insensitive manner"""
        result = bot_controller("Hello", {})
        self.assertEqual(result, "How can I help you?")

        result = bot_controller("HeLLo", {})
        self.assertEqual(result, "How can I help you?")

        result = bot_controller("hello", {})
        self.assertEqual(result, "How can I help you?")

    def test_add_command(self):
        """Handle 'add' command"""
        contacts = {}
        bot_controller("add Ivan 1234", contacts)
        self.assertEqual(contacts, {"Ivan": "1234"})

    def test_change_command(self):
        """Handle 'change' command"""
        contacts = {"Ivan": 1234}
        bot_controller("change Ivan 4321", contacts)
        self.assertEqual(contacts, {"Ivan": "4321"})

    def test_get_contact(self):
        """Handle 'get' command"""
        result = bot_controller("phone Taras", {"Ivan": "1234", "Taras": "2345"})
        self.assertEqual(result, "2345")

    def test_get_all_contact(self):
        """Handle 'all' command"""
        result = bot_controller("all", {"Ivan": "1234", "Taras": "2345"})
        self.assertEqual(result, "Ivan 1234\nTaras 2345")

    def test_invalid_command(self):
        """Handle invalid command"""
        result = bot_controller("test", {})
        self.assertEqual(result, "Invalid command.")
