from app.models import Contact


def parse_input(user_input: str) -> list[str]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    contact = Contact(name=args[0], phone=args[1])
    contacts[contact.name] = contact.phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def get_contact(args: list, contacts: dict) -> str:
    return contacts.get(args[0], "Contact not found.")


def get_all_contacts(contacts: dict) -> str:
    result = ""
    for name, phone in contacts.items():
        result += f"{name} {phone}\n"
    return result.strip()
