from flask import Flask, render_template, abort
import os
import json
app = Flask(__name__)

with open("books.json") as fichero:
    datos=json.load(fichero)


@app.route('/')
def inicio():
    return render_template("inicio.html", datos=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for libro in datos:
        if libro.get("isbn") == isbn:
            return render_template("libro.html", libro=libro)
    abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    return render_template("categoria.html", datos=datos,categoria=categoria)

port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)
