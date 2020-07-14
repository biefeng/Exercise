# *- coding: utf-8 -*
# author BieFeNg
import pymysql

PRODUCT = {'host': '10.128.62.33', 'user': 'root', 'password': 'root', 'database': 'jy_catering'}
PROD_PRODUCT = {'host': '172.16.1.117', 'user': 't11developer', 'password': 'JYwl@2019', 'database': 'jy_product'}
PROD_CATERING = {'host': '172.16.1.106', 'user': 't11developer', 'password': 'JYwl@2019', 'database': 'jy_catering'}
CATERING = {'host': '10.128.62.33', 'user': 'root', 'password': 'root', 'database': 'jy_catering'}

catering_connection = pymysql.connect(host=CATERING['host'], user=CATERING['user'],
                                      password=CATERING['password'],
                                      database=CATERING['database'])
catering_cursor = catering_connection.cursor(cursor=pymysql.cursors.DictCursor)
catering_cursor.execute('SELECT  sku_id ,category_id  FROM catering_sku WHERE shop_id = 99911 ')

with open('d:/update_detail_category_id.sql', 'w') as f:

    for record in catering_cursor.fetchall():
        sql = 'update process_cfg_detail detail  set detail.category_id= ' + str(
            record['category_id']) + ' where sku_id=' + str(record['sku_id']) + ' and shop_id=99911;'
        print(sql)
        print(sql)
        f.write(sql)
        f.write('\r\n')
#
# product_connection = pymysql.connect(host=PROD_PRODUCT['host'], user=PROD_PRODUCT['user'],
#                                      password=PROD_PRODUCT['password'],
#                                      database=PROD_PRODUCT['database'])
# product_cursor = product_connection.cursor(cursor=pymysql.cursors.DictCursor)
# product_cursor.execute(sql)
#
# with open('d:/update_buy_unit.sql', 'w') as f:
#     for record in product_cursor.fetchall():
#         product_id = record['product_id']
#         buy_unit = record['buy_unit']
#         sql = "update sku_store set buy_unit=" + str(buy_unit) + " where sku_id= " + str(product_id) + ";"
#         print(sql)
#         f.write(sql)
#         f.write('\r\n')

catering_connection.close()
# product_connection.close()
