#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import sys
import re
import etcd3

sys.path.append("../")
from meta import *
from utils import printtable
from net import net_pb2, net_pb2_grpc

IP1 = "10.46.234.251"
IP2 = "10.46.234.251"

PORT1 = "8883"
PORT2 = "8885"

_HOST = "localhost"
_PORT = "8883"

etcd = etcd3.client()

publisher_meta = table_meta(
    "Publisher",
    [
        field_meta("id", "int"),
        field_meta("name", "char(100)"),
        field_meta("nation", "char(3)"),
    ],
    [fragment_meta(IP1, PORT1, "db1"), fragment_meta(IP2, PORT2, "db2")],
)


def run():
    conn = grpc.insecure_channel(_HOST + ":" + _PORT)
    client = net_pb2_grpc.NetServiceStub(channel=conn)
    while True:
        text = input("> ")
        if text == "quit" or text == "exit":
            break
        # response = client.SimpleFun(net_pb2.RequestData(text=text))
        # lis = [
        #     net_pb2.SQLTree(sql=text, ip=IP1, port=IP2, dbname="db1"),
        #     net_pb2.SQLTree(sql=text, ip=IP1, port=IP2, dbname="db2"),
        # ]
        print(text)
        table_name = re.findall("from\s+([_A-Za-z]+[0-9]*)\s*;", text)
        print(table_name)
        fragment = eval(etcd.get(table_name[0])[0])
        lis = []
        for request in fragment:
            ip = etcd.get(request["ip"])[0].decode()
            port = etcd.get(request["port"])[0].decode()
            dbname = etcd.get(request["db"])[0].decode()
            lis.append((ip, port, dbname))
        print(str(lis))
        response = client.Excute(net_pb2.SQLTree(sql=text, sites=str(lis)))
        printtable(publisher_meta, eval(response.table))
        # print("received: " + response.table)


if __name__ == "__main__":
    run()
