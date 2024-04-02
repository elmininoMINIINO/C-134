from flask import Flask, render_template
app = Flask(__name__)
#En la función return render_template(‘index.html’)
@app.route("/index")
def first_webpage():
    #Crear una variable
    name = 'Flask'
    # Pasar la variable en la plantilla
    return render_template('index.html', index_variable = name)
app.run(debug=True)



