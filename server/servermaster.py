#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import time
import sys
import re
from concurrent import futures

from pymysql import NULL
from connect import Conndb
import etcd3
import json

sys.path.append("../")
from net import net_pb2, net_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_IP = "10.46.234.251"
_HOST = "localhost"
_PORT = "8883"


class servicer(net_pb2_grpc.NetServiceServicer):
    def __init__(self, sites):
        self.client = {}
        for site in sites:
            if _IP == site["IP"] and _PORT == site["PORT"]:
                self.conndb = Conndb(database=site["DB"])
            else:
                if site["IP"] == _IP:
                    ip = _HOST
                else:
                    ip = site["IP"]
                conn = grpc.insecure_channel(ip + ":" + site["PORT"])
                clientkey = site["IP"] + ":" + site["PORT"] + ":" + site["DB"]
                self.client[clientkey] = net_pb2_grpc.NetServiceStub(channel=conn)

    def Excute(self, request, context):
        tuple_list = []
        sql = request.sql
        lis = eval(request.sites)
        # print(lis)
        for i in lis:
            ip, port, db = i
            # print(ip, port, db)
            # print(ip == _IP)
            # print(port == _PORT)
            if ip == _IP and port == _PORT:
                # print("get local")
                data = self.conndb.read(sql)
                tuple_list += list(data)
            else:
                # print("get remote")
                response = self.client[":".join([ip, port, db])].Excute(
                    net_pb2.SQLTree(sql=sql, sites=str([i]))
                )
                data = eval(response.table)
                tuple_list += list(data)

        return net_pb2.TableData(table=(str(tuple_list)))


def serve():
    print("start server on " + _IP + ":" + _PORT)
    etcd = etcd3.client()
    with open("../config.json") as f:
        config = json.load(f)
    etcd.put("SITES", str(config["SITES"]))
    sites = eval(etcd.get("SITES")[0])
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    net_pb2_grpc.add_NetServiceServicer_to_server(servicer(sites), grpcServer)
    grpcServer.add_insecure_port(_HOST + ":" + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == "__main__":
    if sys.argv[1] != NULL:
        _PORT = sys.argv[1]
    serve()
