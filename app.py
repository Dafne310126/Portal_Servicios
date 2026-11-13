from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compra", methods=["GET", "POST"])
def compra():
    return render_template("compra.html")

@app.route("/salario", methods=["GET", "POST"])
def salario():
    return render_template("salario.html")

@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    return render_template("temperatura.html")

@app.route("/empresa")
def empresa():
    return render_template("empresa.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
