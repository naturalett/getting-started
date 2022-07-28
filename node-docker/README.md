### Create an app
![](examples/architecture_diagram.png)

```bash
cd [path to your node-docker directory]
npm init -y
npm install ronin-server ronin-mocks
touch server.js
```

### Add the server.js
```bash
const ronin     = require( 'ronin-server' )
const mocks     = require( 'ronin-mocks' )
 
const server = ronin.server()
 
server.use( '/', mocks.server( server.Router(), false, true ) )
server.start()
```

### Test the application
```bash
curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{
	"msg": "testing"
}'
{"code":"success","payload":[{"msg":"testing","id":"31f23305-f5d0-4b4f-a16f-6f4c8ec93cf1","createDate":"2020-08-28T21:53:07.157Z"}]}

curl http://localhost:8000/test
{"code":"success","meta":{"total":1,"count":1},"payload":[{"msg":"testing","id":"31f23305-f5d0-4b4f-a16f-6f4c8ec93cf1","createDate":"2020-08-28T21:53:07.157Z"}]}
```

### Build a docker image
```bash
FROM node:12.18.1
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install
COPY . .
CMD [ "node", "server.js" ]
```

### Tag the images
```bash
docker build --tag node-docker .
docker tag node-docker:latest node-docker:v1.0.0
```

### Let's test it
```bash
docker run node-docker

curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{
	"msg": "testing"
}'
curl: (7) Failed to connect to localhost port 8000: Connection refused
```

### Let's export the port
```bash
docker run --publish 8000:8000 node-docker

curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{
	"msg": "testing"
}'
{"code":"success","payload":[{"msg":"testing","id":"dc0e2c2b-793d-433c-8645-b3a553ea26de","createDate":"2020-09-01T17:36:09.897Z"}]}
```

### Run in detached mode
```bash
docker run -d -p 8000:8000 --name app1 node-docker
```

# Nodejs with Mongo

# Create volume, network and mongo
```bash
docker volume create mongodb
docker volume create mongodb_config
docker network create mongodb
docker run -it --rm -d -v mongodb:/data/db \
-v mongodb_config:/data/configdb -p 27017:27017 \
--network mongodb \
--name mongodb \
mongo
```

# Create sever.js
```bash
touch server_mongo.js
# Add the following
const ronin     = require( 'ronin-server' )
const mocks     = require( 'ronin-mocks' )
const database  = require( 'ronin-database' )
const server = ronin.server()
database.connect( process.env.CONNECTIONSTRING )
server.use( '/', mocks.server( server.Router(), false, false ) )
server.start()
```
### Create the Dockerfile
```bash
touch Dockerfile.mongo
# Add
FROM node:12.18.1
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install ronin-database
COPY . .
CMD [ "node", "server_mongo.js" ]
```

### Build the image
```bash
docker build --tag node-docker-mongo -f Dockerfile.mongo .
```

### Run the app-2
```bash
docker run \
-it --rm -d \
--network mongodb \
--name rest-server \
-p 8001:8000 \
-e CONNECTIONSTRING=mongodb://mongodb:27017/yoda_notes \
node-docker-mongo
```

### Test it
```bash
curl --request POST \
--url http://localhost:8001/notes \
--header 'content-type: application/json' \
--data '{
"name": "this is a note",
"text": "this is a note that I wanted to take while I was working on writing a blog post.",
"owner": "peter"
}'
```

### Docker compose
```bash
docker-compose -f docker-compose.dev.yml up --build
```

[part-i](https://www.docker.com/blog/getting-started-with-docker-using-node-jspart-i/)

[part-ii](https://www.docker.com/blog/getting-started-with-docker-using-node-part-ii/)