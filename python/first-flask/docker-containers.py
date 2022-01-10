import docker

client = docker.from_env()

print(f'client: {client}')
# result = client.containers.run("ubuntu", "echo hello world")
# client.containers.run("bfirsh/reticulate-splines", detach=True)
# result = client.containers.list()
container = client.containers.get('magical_wilbur')

result = container.attrs

print(result)
