# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.email_msg import email_msg_pb2 as email__msg__pb2


class EmailStub(object):
    """定义Hello服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendEmail = channel.unary_unary(
                '/Email/SendEmail',
                request_serializer=email__msg__pb2.SendEmailRequest.SerializeToString,
                response_deserializer=email__msg__pb2.SendEmailResponse.FromString,
                )


class EmailServicer(object):
    """定义Hello服务
    """

    def SendEmail(self, request, context):
        """定义SayHello方法
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.SendEmail,
                    request_deserializer=email__msg__pb2.SendEmailRequest.FromString,
                    response_serializer=email__msg__pb2.SendEmailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Email', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Email(object):
    """定义Hello服务
    """

    @staticmethod
    def SendEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Email/SendEmail',
            email__msg__pb2.SendEmailRequest.SerializeToString,
            email__msg__pb2.SendEmailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
