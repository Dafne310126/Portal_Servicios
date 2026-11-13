
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Portal de Servicios</h1>
    <p>Mi aplicación Flask está funcionando correctamente.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
