# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from net import net_pb2 as net_dot_net__pb2


class NetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimpleFun = channel.unary_unary(
                '/net.NetService/SimpleFun',
                request_serializer=net_dot_net__pb2.RequestData.SerializeToString,
                response_deserializer=net_dot_net__pb2.ResponseData.FromString,
                )
        self.Excute = channel.unary_unary(
                '/net.NetService/Excute',
                request_serializer=net_dot_net__pb2.SQLTree.SerializeToString,
                response_deserializer=net_dot_net__pb2.TableData.FromString,
                )


class NetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimpleFun(self, request, context):
        """test method
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Excute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimpleFun': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleFun,
                    request_deserializer=net_dot_net__pb2.RequestData.FromString,
                    response_serializer=net_dot_net__pb2.ResponseData.SerializeToString,
            ),
            'Excute': grpc.unary_unary_rpc_method_handler(
                    servicer.Excute,
                    request_deserializer=net_dot_net__pb2.SQLTree.FromString,
                    response_serializer=net_dot_net__pb2.TableData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'net.NetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimpleFun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/SimpleFun',
            net_dot_net__pb2.RequestData.SerializeToString,
            net_dot_net__pb2.ResponseData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Excute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Excute',
            net_dot_net__pb2.SQLTree.SerializeToString,
            net_dot_net__pb2.TableData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
