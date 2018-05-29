import grpc
import os
from concurrent import futures
from dotenv import load_dotenv
from ml import ml_pb2_grpc
from ml import runner


class Boxer(ml_pb2_grpc.BoxerServicer):
    def Run(self, request, context):
        return runner.launch()


def serve():
    load_dotenv()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ml_pb2_grpc.add_BoxerServicer_to_server(Boxer(), server)
    server.add_insecure_port('[::]:%s' % os.getenv("PORT"))
    try:
        server.start()
        print("Serving ...")
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)
        print("Stop ...")


if __name__ == '__main__':
    serve()
