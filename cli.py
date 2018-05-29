import os
import grpc
from dotenv import load_dotenv
from ml import ml_pb2_grpc
from ml import ml_pb2


def run():
    channel = grpc.insecure_channel('localhost:%s' % os.getenv('PORT'))
    stub = ml_pb2_grpc.BoxerStub(channel=channel)
    response = stub.Run(request=ml_pb2.ArtifactRequest())  # type: ml_pb2.Artifact
    print(response.uuid)


if __name__ == '__main__':
    load_dotenv()
    run()
