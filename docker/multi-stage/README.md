## Getting Started

The example here again uses the official maven base image to run first stage of the build using a desired version of Maven. The second stage, I'm using Google's distroless base image, which strives to provide just enough run-time for a java app.

This example uses a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/)

Extract the content: https://start.spring.io/

## Build the image

```BASH
docker build -t demo .
```

## Run the application

```BASH
docker run --rm -it demo:latest
```

## Misc

```BASH
Read the Docker hub documentation on how the Maven build can be optimized to use a local repository to cache jars.

https://hub.docker.com/_/maven
```

## Reusing the Maven local repository
### Or you can just use your home .m2 cache directory that you share e.g. with your Eclipse/IDEA:

```BASH
$ docker run -it --rm -v "$PWD":/usr/src/mymaven -v "$HOME/.m2":/root/.m2 -v "$PWD/target:/usr/src/mymaven/target" -w /usr/src/mymaven maven mvn clean package  

```
