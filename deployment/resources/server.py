#!/usr/bin/env python3
from flask import Flask, request, url_for, redirect
import os
import sys

index_path = os.environ.get("INDEX_PATH", ".")
app = Flask(__name__, static_folder=index_path)


@app.route("/", methods=["GET", "POST"])
def echo():
    """
    Message order:
    1. URI parameter: "/?message=my_message"
    2. Request body "message=my_message"
    3. JSON Object: {"message": "my_message"}
    4. Request header: "message: my_message"
    """
    message_string = "message"
    response_obj = {}
    response_obj["server_address"] = request.host
    response_obj["request_address"] = request.remote_addr
    if request.method == "GET":
        message = request.args.get(message_string)
    else:
        message = request.values.get(message_string)
        if not message:
            try:
                message = request.json.get("message")
            except Exception:
                print("Could not parse json")
    if not message:
        message = request.headers.get(message_string)
    response_obj[message_string] = message
    return response_obj


@app.route("/index.html")
def serve_index():
    index_full_path = os.path.join(index_path, "index.html")
    if os.path.isfile(index_full_path):
        print(f"{index_full_path} exists, serving index.html")
        return app.send_static_file("index.html")
    else:
        print(f"{index_full_path} does not exists, redirecting to /")
        return redirect(url_for("echo"))


if __name__ == "__main__":
    from waitress import serve
    from paste.translogger import TransLogger

    serve(TransLogger(app), host="0.0.0.0", port=8080)
