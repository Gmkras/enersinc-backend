from typing import List

from .connection import _fetch_all, _fetch_lastrow_id, _fetch_none, _fetch_one
from ..models.models import Persona
from ..models.exceptions import UserAlreadyExists, UserNotFound

from faker import Faker


def create(persona: Persona) -> Persona:
    if user_exists("email", persona.email):
        raise UserAlreadyExists(f"Email {persona.email} is already used")

    query = """INSERT INTO personas VALUES (:nombres, :apellidos,
                                            :tipo_documento, :documento, :email,
                                            :hobbie)"""

    persona_dict = persona._asdict()

    id_ = _fetch_lastrow_id(query, persona_dict)

    persona_dict["id"] = id_
    return Persona(**persona_dict)


def update(persona: Persona) -> Persona:
    if not user_exists("oid", persona.id):
        raise UserNotFound("Persona not Found!")

    query = """UPDATE personas SET nombres = :nombres, apellidos = :apellidos,
                      tipo_documento = :tipo_documento, documento = :documento, email = :email,
                      hobbie = :hobbie
               WHERE oid = :oid"""

    parameters = persona._asdict()

    _fetch_none(query, parameters)

    return persona


def delete(persona: Persona) -> Persona:
    if not user_exists("oid", persona.id):
        raise UserNotFound("persona not Found!")

    query = "DELETE FROM personas WHERE oid = ?"
    parameters = [persona.id]

    _fetch_none(query, parameters)

    return persona


def list_all() -> List[Persona]:
    query = "SELECT oid, * FROM personas"
    records = _fetch_all(query)

    personas = []
    for record in records:
        persona = Persona(id=record[0], nombres=record[1], apellidos=record[2],
                          tipo_documento=record[3], documento=record[4], email=record[5],
                          hobbie=record[6])
        personas.append(persona)

    return personas


def detail(persona: Persona) -> Persona:
    query = "SELECT oid, * FROM personas WHERE oid=?"
    parameters = [persona.id]

    record = _fetch_one(query, parameters)

    if record is None:
        raise UserNotFound(f"No user with id: {persona.id}")

    persona = Persona(id=record[0], nombres=record[1], apellidos=record[2],
                      tipo_documento=record[3], documento=record[4], email=record[5],
                      hobbie=record[6])
    
    return persona


def user_exists(field: str, value: str) -> bool:
    query = f"SELECT oid, email FROM personas WHERE {field}=?"
    parameters = [value]

    record = _fetch_one(query, parameters)

    return bool(record)


def reset_table() -> None:
    query = "DROP TABLE IF EXISTS personas"
    _fetch_none(query)

    fields = """(nombres text, apellidos text, tipo_documento text, documento text,
                 email text, hobbie text)"""
    query = f"CREATE TABLE IF NOT EXISTS personas {fields}"

    _fetch_none(query)

    fake = Faker()
    fake.seed_instance(42)

    for _ in range(10):
        test_user = Persona(nombres=fake.first_name(),
                            apellidos=fake.last_name(),
                            tipo_documento=fake.street_address(),
                            documento=fake.postcode(),
                            email=fake.email(),
                            hobbie=fake.phone_number())

        create(test_user)