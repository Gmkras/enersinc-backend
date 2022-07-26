from typing import NamedTuple, Optional

class Persona(NamedTuple):
    id: Optional[int] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    tipo_documento: Optional[str] = None
    documento: Optional[str] = None
    email: Optional[str] = None
    hobbie: Optional[str] = None