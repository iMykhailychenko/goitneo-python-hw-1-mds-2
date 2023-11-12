from datetime import date

from pydantic import BaseModel


class Birthday(BaseModel):
    name: str
    birthday: date


class Contact(BaseModel):
    name: str
    phone: str
