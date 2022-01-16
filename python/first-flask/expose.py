import docker
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    containerName = request.args.get("containerName", "")
    if containerName:
        status, name = container_status(containerName)
    else:
        status, name = "", ""
    return (
            """<form action="" method="get">
                    Container Name: <input type="text" name="containerName">
                    <input type="submit" value="What is my docker status">
                </form>"""
            + "Container Status: "
            + status
            + "<br><br>Name: "
            + name
    )


def container_status(containerName):
    try:
        client = docker.from_env()
        container = client.containers.get(containerName)
        status = container.attrs['State']['Status']
        name = container.attrs['Name']
        print(f'container.attrs: {container.attrs}')
        print(f'Status: {status}')
        return status, name
    except(Exception):
        return "Invalid input", containerName


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
