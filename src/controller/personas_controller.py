from typing import List

from ..database import personas
from ..models.models import Persona
from ..helpers import helper


def create(persona_: Persona) -> Persona:
    persona = helper.format_name(persona_)
    helper.validate_persona(persona)
    return personas.create(persona)

def update(persona: Persona) -> Persona:
    persona = helper.format_name(persona)
    helper.validate_persona(persona)
    return personas.update(persona)

def delete(persona: Persona) -> Persona:
    return personas.delete(persona)

def lists() -> List[Persona]:
    return personas.list_all()

def details(persona: Persona) -> Persona:
    return personas.detail(persona)