from typing import Union

from app.bot.services import (add_contact, change_contact, get_all_contacts,
                              get_contact, parse_input)


def bot_controller(user_input: str, contacts: dict) -> Union[str, None]:
    cmd, *args = parse_input(user_input)

    if cmd == "add":
        return add_contact(args, contacts)
    elif cmd == "change":
        return change_contact(args, contacts)
    elif cmd == "phone":
        return get_contact(args, contacts)
    elif cmd == "all":
        return get_all_contacts(contacts)
    elif cmd == "hello":
        return "How can I help you?"
    elif cmd == "exit" or cmd == "close":
        return None
    else:
        return "Invalid command."
