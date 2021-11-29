import etcd3

etcd = etcd3.client()

jdata = {
    "IP1": "10.46.234.251",
    "IP2": "10.46.234.251",
    "PORT1": "8883",
    "PORT2": "8885",
    "DB1": "db1",
    "DB2": "db2",
}

for j in jdata:
    etcd.put(j, jdata[j])

for j in jdata:
    print(etcd.get(j))

table_metas = {
    "table_list": ["Publisher"],
    "Publisher": [
        {"ip": "IP1", "port": "PORT1", "db": "DB1"},
        {"ip": "IP2", "port": "PORT2", "db": "DB2"},
    ],
}

for i in table_metas["table_list"]:
    etcd.put(i, str(table_metas[i]))

for i in table_metas["table_list"]:
    print(etcd.get(i))

# for j in jdata:
#     etcd.delete(j)
