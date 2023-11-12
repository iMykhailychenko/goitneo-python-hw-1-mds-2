import os
from pathlib import Path

from app.models import Birthday

users_path = Path(os.getcwd(), "assets", "users.csv")


def get_users_list() -> list[Birthday]:
    with open(users_path, "r") as f:
        users = []
        while True:
            line = f.readline()
            if not line:
                break
            name, birthday = line.strip().split(",")
            users.append(Birthday(name=name, birthday=birthday))

        return users
