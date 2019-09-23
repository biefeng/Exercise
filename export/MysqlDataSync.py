# *- coding: utf-8 -*
# author BieFeNg

import pymysql

DEV = {'host': '10.128.62.33', 'user': 'root', 'password': 'root', 'database': 'jy_catering'}


class data_sync:
    def __init__(self):
        self.column_name = "("
        self.values=[]

    def get_cursor(self, **kwargs):
        # connection = pymysql.connect(host="10.128.62.33", usser="root", password="root", database="jy_catering")
        connection = pymysql.connect(host=kwargs['host'], user=kwargs['user'], password=kwargs['password'],
                                     database=kwargs['database'])
        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor

    def m(self):
        sale_stk_cursor = self.get_cursor(**DEV)
        sale_stk_cursor.execute("select * from stk_sku")
        all = sale_stk_cursor.fetchall()
        for item in all:
            for k,v in item.items():
                self.column_name.append("'"+k+"'")
                self.values.append(v)

        print(all.__len__())


data_sync().m()
