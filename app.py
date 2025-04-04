from flask import Flask, render_template

app = Flask(__name__) #slo se va a ejecutar aesta variable para este programa llamado app.py

@app.route('/') #decorador, se le dice a flask que la funcion home es la que se va a ejecutar cuando se acceda a la ruta /
def home():
    return render_template('index.html')
#se renderiza el template index.html que se encuentra en la carpeta templates

if __name__ == '__main__':    #si el nombre del modulo es __main__, se ejecuta la app 0
    app.run(debug=True)      #se ejecuta la app en modo debug, para que se reinicie automaticamente cuando se hagan cambios en el codigo