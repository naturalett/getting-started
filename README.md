## Build the image

```BASH
docker build -t hello_world .
```

## Validate the image

```BASH
docker images
```

## Access the application

```BASH
docker run -it hello_world bash
```

## Run the application

```BASH
docker run hello_world
```

## Run the application in the background

```BASH
docker run -d --name=hello_world hello_world
```

## Check your container

```BASH
docker ps -a
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