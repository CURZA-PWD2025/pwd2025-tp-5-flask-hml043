from flask import Flask, render_template
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/productos")
def listar_productos():
    return render_template('productos.html', productos=productos)

@app.route("/categorias")
def listar_categorias():
    return render_template('categorias.html', categorias=categorias)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)