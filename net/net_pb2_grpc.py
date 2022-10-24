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
        self.Test = channel.unary_unary(
                '/net.NetService/Test',
                request_serializer=net_dot_net__pb2.Data.SerializeToString,
                response_deserializer=net_dot_net__pb2.Data1.FromString,
                )
        self.Createtable = channel.unary_unary(
                '/net.NetService/Createtable',
                request_serializer=net_dot_net__pb2.SQL.SerializeToString,
                response_deserializer=net_dot_net__pb2.Status.FromString,
                )
        self.Droptable = channel.unary_unary(
                '/net.NetService/Droptable',
                request_serializer=net_dot_net__pb2.SQL.SerializeToString,
                response_deserializer=net_dot_net__pb2.Status.FromString,
                )
        self.Loaddata = channel.unary_unary(
                '/net.NetService/Loaddata',
                request_serializer=net_dot_net__pb2.LoadParams.SerializeToString,
                response_deserializer=net_dot_net__pb2.Status.FromString,
                )
        self.Insertdata = channel.unary_unary(
                '/net.NetService/Insertdata',
                request_serializer=net_dot_net__pb2.LoadParams.SerializeToString,
                response_deserializer=net_dot_net__pb2.DataReturn.FromString,
                )
        self.Deletedata = channel.unary_unary(
                '/net.NetService/Deletedata',
                request_serializer=net_dot_net__pb2.SQL.SerializeToString,
                response_deserializer=net_dot_net__pb2.DataReturn.FromString,
                )
        self.SimpleSelect = channel.unary_unary(
                '/net.NetService/SimpleSelect',
                request_serializer=net_dot_net__pb2.SQL.SerializeToString,
                response_deserializer=net_dot_net__pb2.SimpleSelectReturn.FromString,
                )
        self.Excute = channel.unary_unary(
                '/net.NetService/Excute',
                request_serializer=net_dot_net__pb2.SQLTree.SerializeToString,
                response_deserializer=net_dot_net__pb2.TableData.FromString,
                )
        self.jr_grpc_test = channel.unary_unary(
                '/net.NetService/jr_grpc_test',
                request_serializer=net_dot_net__pb2.para_jr_grpc_test.SerializeToString,
                response_deserializer=net_dot_net__pb2.ret_jr_grpc_test.FromString,
                )
        self.grpc_dfs = channel.unary_unary(
                '/net.NetService/grpc_dfs',
                request_serializer=net_dot_net__pb2.para_grpc_dfs.SerializeToString,
                response_deserializer=net_dot_net__pb2.ret_grpc_dfs.FromString,
                )
        self.start_jr = channel.unary_unary(
                '/net.NetService/start_jr',
                request_serializer=net_dot_net__pb2.para_start_jr.SerializeToString,
                response_deserializer=net_dot_net__pb2.ret_start_jr.FromString,
                )
        self.temp_GC = channel.unary_unary(
                '/net.NetService/temp_GC',
                request_serializer=net_dot_net__pb2.para_temp_GC.SerializeToString,
                response_deserializer=net_dot_net__pb2.ret_temp_GC.FromString,
                )
        self.createdatabase = channel.unary_unary(
                '/net.NetService/createdatabase',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.dbres.FromString,
                )
        self.dropdatabase1 = channel.unary_unary(
                '/net.NetService/dropdatabase1',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.dbres.FromString,
                )
        self.dropdatabase2 = channel.unary_unary(
                '/net.NetService/dropdatabase2',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.dbres.FromString,
                )
        self.dropdatabase3 = channel.unary_unary(
                '/net.NetService/dropdatabase3',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.usedbres.FromString,
                )
        self.usedatabase1 = channel.unary_unary(
                '/net.NetService/usedatabase1',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.dbres.FromString,
                )
        self.usedatabase2 = channel.unary_unary(
                '/net.NetService/usedatabase2',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.dbres.FromString,
                )
        self.usedatabase3 = channel.unary_unary(
                '/net.NetService/usedatabase3',
                request_serializer=net_dot_net__pb2.para_dbname.SerializeToString,
                response_deserializer=net_dot_net__pb2.usedbres.FromString,
                )
        self.jr_exit = channel.unary_unary(
                '/net.NetService/jr_exit',
                request_serializer=net_dot_net__pb2.para_jr_exit.SerializeToString,
                response_deserializer=net_dot_net__pb2.ret_jr_exit.FromString,
                )


class NetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Test(self, request, context):
        """test method
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Createtable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Droptable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Loaddata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insertdata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deletedata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SimpleSelect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Excute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def jr_grpc_test(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def grpc_dfs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def start_jr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def temp_GC(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createdatabase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dropdatabase1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dropdatabase2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dropdatabase3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def usedatabase1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def usedatabase2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def usedatabase3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def jr_exit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Test': grpc.unary_unary_rpc_method_handler(
                    servicer.Test,
                    request_deserializer=net_dot_net__pb2.Data.FromString,
                    response_serializer=net_dot_net__pb2.Data1.SerializeToString,
            ),
            'Createtable': grpc.unary_unary_rpc_method_handler(
                    servicer.Createtable,
                    request_deserializer=net_dot_net__pb2.SQL.FromString,
                    response_serializer=net_dot_net__pb2.Status.SerializeToString,
            ),
            'Droptable': grpc.unary_unary_rpc_method_handler(
                    servicer.Droptable,
                    request_deserializer=net_dot_net__pb2.SQL.FromString,
                    response_serializer=net_dot_net__pb2.Status.SerializeToString,
            ),
            'Loaddata': grpc.unary_unary_rpc_method_handler(
                    servicer.Loaddata,
                    request_deserializer=net_dot_net__pb2.LoadParams.FromString,
                    response_serializer=net_dot_net__pb2.Status.SerializeToString,
            ),
            'Insertdata': grpc.unary_unary_rpc_method_handler(
                    servicer.Insertdata,
                    request_deserializer=net_dot_net__pb2.LoadParams.FromString,
                    response_serializer=net_dot_net__pb2.DataReturn.SerializeToString,
            ),
            'Deletedata': grpc.unary_unary_rpc_method_handler(
                    servicer.Deletedata,
                    request_deserializer=net_dot_net__pb2.SQL.FromString,
                    response_serializer=net_dot_net__pb2.DataReturn.SerializeToString,
            ),
            'SimpleSelect': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleSelect,
                    request_deserializer=net_dot_net__pb2.SQL.FromString,
                    response_serializer=net_dot_net__pb2.SimpleSelectReturn.SerializeToString,
            ),
            'Excute': grpc.unary_unary_rpc_method_handler(
                    servicer.Excute,
                    request_deserializer=net_dot_net__pb2.SQLTree.FromString,
                    response_serializer=net_dot_net__pb2.TableData.SerializeToString,
            ),
            'jr_grpc_test': grpc.unary_unary_rpc_method_handler(
                    servicer.jr_grpc_test,
                    request_deserializer=net_dot_net__pb2.para_jr_grpc_test.FromString,
                    response_serializer=net_dot_net__pb2.ret_jr_grpc_test.SerializeToString,
            ),
            'grpc_dfs': grpc.unary_unary_rpc_method_handler(
                    servicer.grpc_dfs,
                    request_deserializer=net_dot_net__pb2.para_grpc_dfs.FromString,
                    response_serializer=net_dot_net__pb2.ret_grpc_dfs.SerializeToString,
            ),
            'start_jr': grpc.unary_unary_rpc_method_handler(
                    servicer.start_jr,
                    request_deserializer=net_dot_net__pb2.para_start_jr.FromString,
                    response_serializer=net_dot_net__pb2.ret_start_jr.SerializeToString,
            ),
            'temp_GC': grpc.unary_unary_rpc_method_handler(
                    servicer.temp_GC,
                    request_deserializer=net_dot_net__pb2.para_temp_GC.FromString,
                    response_serializer=net_dot_net__pb2.ret_temp_GC.SerializeToString,
            ),
            'createdatabase': grpc.unary_unary_rpc_method_handler(
                    servicer.createdatabase,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.dbres.SerializeToString,
            ),
            'dropdatabase1': grpc.unary_unary_rpc_method_handler(
                    servicer.dropdatabase1,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.dbres.SerializeToString,
            ),
            'dropdatabase2': grpc.unary_unary_rpc_method_handler(
                    servicer.dropdatabase2,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.dbres.SerializeToString,
            ),
            'dropdatabase3': grpc.unary_unary_rpc_method_handler(
                    servicer.dropdatabase3,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.usedbres.SerializeToString,
            ),
            'usedatabase1': grpc.unary_unary_rpc_method_handler(
                    servicer.usedatabase1,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.dbres.SerializeToString,
            ),
            'usedatabase2': grpc.unary_unary_rpc_method_handler(
                    servicer.usedatabase2,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.dbres.SerializeToString,
            ),
            'usedatabase3': grpc.unary_unary_rpc_method_handler(
                    servicer.usedatabase3,
                    request_deserializer=net_dot_net__pb2.para_dbname.FromString,
                    response_serializer=net_dot_net__pb2.usedbres.SerializeToString,
            ),
            'jr_exit': grpc.unary_unary_rpc_method_handler(
                    servicer.jr_exit,
                    request_deserializer=net_dot_net__pb2.para_jr_exit.FromString,
                    response_serializer=net_dot_net__pb2.ret_jr_exit.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'net.NetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Test',
            net_dot_net__pb2.Data.SerializeToString,
            net_dot_net__pb2.Data1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Createtable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Createtable',
            net_dot_net__pb2.SQL.SerializeToString,
            net_dot_net__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Droptable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Droptable',
            net_dot_net__pb2.SQL.SerializeToString,
            net_dot_net__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Loaddata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Loaddata',
            net_dot_net__pb2.LoadParams.SerializeToString,
            net_dot_net__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insertdata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Insertdata',
            net_dot_net__pb2.LoadParams.SerializeToString,
            net_dot_net__pb2.DataReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deletedata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/Deletedata',
            net_dot_net__pb2.SQL.SerializeToString,
            net_dot_net__pb2.DataReturn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SimpleSelect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/SimpleSelect',
            net_dot_net__pb2.SQL.SerializeToString,
            net_dot_net__pb2.SimpleSelectReturn.FromString,
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

    @staticmethod
    def jr_grpc_test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/jr_grpc_test',
            net_dot_net__pb2.para_jr_grpc_test.SerializeToString,
            net_dot_net__pb2.ret_jr_grpc_test.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def grpc_dfs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/grpc_dfs',
            net_dot_net__pb2.para_grpc_dfs.SerializeToString,
            net_dot_net__pb2.ret_grpc_dfs.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def start_jr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/start_jr',
            net_dot_net__pb2.para_start_jr.SerializeToString,
            net_dot_net__pb2.ret_start_jr.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def temp_GC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/temp_GC',
            net_dot_net__pb2.para_temp_GC.SerializeToString,
            net_dot_net__pb2.ret_temp_GC.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createdatabase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/createdatabase',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.dbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dropdatabase1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/dropdatabase1',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.dbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dropdatabase2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/dropdatabase2',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.dbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dropdatabase3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/dropdatabase3',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.usedbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def usedatabase1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/usedatabase1',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.dbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def usedatabase2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/usedatabase2',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.dbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def usedatabase3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/usedatabase3',
            net_dot_net__pb2.para_dbname.SerializeToString,
            net_dot_net__pb2.usedbres.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def jr_exit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.NetService/jr_exit',
            net_dot_net__pb2.para_jr_exit.SerializeToString,
            net_dot_net__pb2.ret_jr_exit.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
