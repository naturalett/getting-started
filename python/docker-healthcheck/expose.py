from flask import Flask
from flask import request
import docker

app = Flask(__name__)


@app.route("/")
def index():
    container_name = request.args.get("container_name", "")
    if container_name:
        container_status, port = get_container_status_by_name(container_name)
    else:
        container_status = ""
        port = ""
    return (
            """<form action="" method="get">
                    Place the container name: <input type="text" name="container_name">
                    <input type="submit" value="Convert to Fahrenheit">
                </form>"""
            + "<b>Status: </b>"
            + container_status
            + "<br><br><b>Container name: </b>"
            + container_name
            + "<br><br><b>Port is: </b>"
            + port
    )


def get_container_status_by_name(container_name):
    """Get container status by name"""
    try:
        client = docker.from_env()
        container = client.containers.get(container_name)
        status = container.attrs['State']['Status']
        if (status == "exited"):
            return "NotAvailable", "0"
        port = container.attrs['NetworkSettings']['Ports']
        print(f"Container name is: {container}")
        print(f"Container status is: {status}")
        print(f"result is: {port}")
        print(f"Port is: {list(port.keys())[0]}")

        return str(status), str(port)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="0.0.0.0")


# https://github.com/docker/docker-py
# https://realpython.com/python-web-applications/