# Docker Healthcheck

## Run a docker test container
```
docker container run -name dockertest -it -d alpine /bin/sh
```

## Run the flask server
```
python expose.py
```
Checkout the http://localhost:5000

## Run the flask server as Docker container
### Build the Dockerfile
```
docker build -t docker-healthcheck .
```
### Run the docker container
```
docker run -d -p 5000:5000 --name docker-healthcheck docker-healthcheck:latest
```

## References
[docker-py](https://github.com/docker/docker-py) \
[python-web-applications](https://realpython.com/python-web-applications/)
