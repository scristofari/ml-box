import docker
from . import ml_pb2


def launch(path: str = "./ml/fixtures", tag: str = "ml-box") -> ml_pb2.Artifact:
    client = docker.from_env()
    (img, logs) = client.images.build(path=path, tag=tag)

    print(img)
    for l in enumerate(logs):
        if 'stream' in l[1]:
            print(l[1]['stream'])

    output = client.containers.run(image=img)
    print(output)

    client.close()

    artifact = ml_pb2.Artifact()
    artifact.uuid = 'test'
    artifact.status = "pending"

    return artifact
