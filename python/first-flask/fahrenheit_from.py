from flask import Flask

app = Flask(__name__)


# decorator
@app.route("/")
def index():
    return "Web App"


# decorator
@app.route("/<celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except(Exception):
        print("Invalid input")
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
