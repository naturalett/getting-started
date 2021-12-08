## Build the image

```BASH
docker build -t hello_world .
```

## Validate the image

```BASH
docker images
```

## Run the application in the background

```BASH
docker run -p 8181:81 -d --name=hello_world hello_world
```

#### 81 -> destination (inside the docker \ the flask app)
#### 8181 -> source (the outside port)

## Check your application

```BASH
http://<IP>:81
```

## Check the logs

```BASH
docker logs hello_world
```
#### to tail the logs we can use --follow


## Kill the application

```BASH
docker stop hello_world && docker rm hello_world
```