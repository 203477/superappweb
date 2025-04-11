from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__) #slo se va a ejecutar aesta variable para este programa llamado app.py

catalogo = [
    {'id': 1, 'nombre': 'pan', 'precio': 20},
    {'id': 2, 'nombre': 'leche', 'precio': 30},
    {'id': 3, 'nombre': 'huevos', 'precio': 50},
    {'id': 4, 'nombre': 'queso', 'precio': 80},
    {'id': 5, 'nombre': 'mantequilla', 'precio': 60},
    {'id': 6, 'nombre': 'azúcar', 'precio': 25},
    {'id': 7, 'nombre': 'café', 'precio': 100},
    {'id': 8, 'nombre': 'arroz', 'precio': 40},
    {'id': 9, 'nombre': 'frijoles', 'precio': 35},
    {'id': 10, 'nombre': 'harina', 'precio': 45},
]


@app.route('/') #decorador, se le dice a flask que la funcion home es la que se va a ejecutar cuando se acceda a la ruta /
def home():
    print(catalogo)
    return render_template('index.html', productos=catalogo) #se llama a la funcion render_template, que se encarga de renderizar el template y pasarle los datos necesarios, en este caso, la lista catalogo.
#se le pasa la lista catalogo a la plantilla index.html, para que esta pueda acceder a los datos y mostrarlos en la pagina web
#se renderiza el template index.html que se encuentra en la carpeta templates

@app.route('/producto/<int:id>') #decorador, se le dice a flask que la funcion producto es la que se va a ejecutar cuando se acceda a la ruta /producto/<id>, donde <id> es un entero
def agregar(id):
    if 'carrito' not in session:
        session['carrito'] = [] #se verifica si la variable de sesion carrito no existe, si no existe, se crea una lista vacia
    session['carrito'].append(id)
    session.modified = True
    return redirect(url_for('home'))

if __name__ == '__main__':    #si el nombre del modulo es __main__, se ejecuta la app 0
    app.run(debug=True)      #se ejecuta la app en modo debug, para que se reinicie automaticamente cuando se hagan cambios en el codigo
