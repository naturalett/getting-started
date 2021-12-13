## Build the image

```BASH
docker build -t nginx:v1 .
```

## Validate the image

```BASH
docker images | grep nginx
```

## Run the application in the background

```BASH
docker run -it -d -p 8080:80 --name web nginx:v1
```

## Check that your request is being blocked

```BASH
curl -I http://localhost:8080 -H 'User-Agent: ${jndi:'
```

## Access the nginx

```BASH
http://localhost:8080/
```
