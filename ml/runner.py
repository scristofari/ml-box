import docker


def go():
    client = docker.from_env()
    client.close()