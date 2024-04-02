#Importar el módulo Flask en el proyecto.
from flask import Flask

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"

#Definir una función con diferente punto final.

@app.route("/flask_2")
def second_flask():
    return "¡Python es divertido!"

#Ejecutamos usando un argumento depurativo (debug).
app.run(debug=True)

