from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)

nav = [
    {"name": "Listar Todos", "url":"/api/personas"},
    {"name": "Persona ID", "url":"/api/personas/1"},
]

@global_scope.route("/", methods=['GET'])
def home():
    
    parameters = {"title": "Plantilla flask",
                  "description": "this is a simple page"
                  }
    
    return render_template("home.html", nav=nav, **parameters)