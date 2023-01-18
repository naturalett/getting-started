import flask
app = flask.Flask(__name__)

@app.route('/home')
def home():
    return 'Hello, World!'

@app.route("/", methods=["GET", "POST"])
def response():
    # print(requests)
    if flask.request.method == "POST":
        return "POST method called"
    return "GET method called"
