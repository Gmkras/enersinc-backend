import re

from ..models.models import Persona
from ..models.exceptions import UserNotValid


def validate_persona(persona: Persona) -> None:
    if not __email_is_valid(persona.email):
        raise UserNotValid(f"The email address: {persona.email} is not valid")

    if None in (persona.nombres, persona.apellidos, persona.email):
        raise UserNotValid("The user has no first name, last name or email")


def format_name(persona: Persona) -> Persona:
    persona_dict = persona._asdict()
    persona_dict["nombres"] = persona.nombres.capitalize()
    persona_dict["apellidos"] = persona.nombres.capitalize()

    return Persona(**persona_dict)


def __email_is_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, email))