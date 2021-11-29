from meta import *


def printtable(table_meta: table_meta, data: tuple):
    for field_meta in table_meta.field_meta_list:
        print("| %s " % field_meta.name, end=" ")
    print("|")
    for item in data:
        for i in item:
            print("| %s " % str(i), end=" ")
        print("|")
    print("return: ", len(data), " lines")
