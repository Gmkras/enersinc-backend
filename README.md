# enersinc-backend
prueba tecnica para enersinc, backend con flask

crear entorno virtual con venv

crear un .env con dos variables de entorno con nombres SECRET,DB_TOKEN, una para el secret key de jwt y el otro para encryptar la base de datos (metodo no muy seguro pero igual da seguridad extra),
base de datos manejada en sqlite3.

con el ambiente virtual activado instalar dependencias que estan en los requeriments.txt.

se puede ejecutar el servidos con los comandos.
python run.py
python -m src

solo se maneja un modelo que es el de persona que fue el requerido y el jwt se genera con el email del usuario (se intenta implementar jwt).