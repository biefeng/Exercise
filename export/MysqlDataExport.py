# *- coding=utf-8 -*
import getopt
import sys
import pymysql
from xlwt import Workbook, XFStyle, Font, Borders, Pattern, Style, Alignment
from csv import DictWriter

DEV = {'host': '10.128.62.33', 'user': 'root', 'password': 'root', 'database': 'jy_catering'}
BASE_WIN_OUTPUT_PATH = 'd:/'
profiles = {'dev': DEV}


class Export:
    def export_to_csv(self, **kwargs):
        limit = 10000
        count = self.get_data_scale(**kwargs)['count']
        times = (count + limit - 1) // limit

        add_header = False
        for i in range(times):
            kwargs["startIndex"] = i * limit + 1
            kwargs['endIndex'] = (i + 1) * limit + 1

            records = self.get_data(**kwargs)
            with open(kwargs['table'] + '.csv', 'w', newline='') as csvfile:
                dict_writer = None
                column_names = []

                for data in records:
                    if not add_header:
                        for column_name in data.keys():
                            column_names.append(column_name)
                        add_header = True
                        dict_writer = DictWriter(csvfile, fieldnames=column_names, delimiter=" ")
                        dict_writer.writeheader()
                    dict_writer.writerow(data)

    def export_to_excel(self, **kwargs):
        work_book = Workbook(encoding="ascii")
        center_alignment = Alignment()
        center_alignment.horz = Alignment.HORZ_RIGHT
        center_alignment.vert = Alignment.VERT_CENTER

        border = Borders()
        border.top = Borders.THIN
        border.left = Borders.THIN
        border.bottom = Borders.THIN
        border.right = Borders.THIN

        head_style = XFStyle()

        head_pattern = Pattern()
        head_pattern.pattern = Pattern.SOLID_PATTERN
        head_pattern.pattern_fore_colour = Style.colour_map['gray25']

        head_style.pattern = head_pattern

        head_font = Font()
        head_font.bold = True
        head_style.font = head_font

        head_style.alignment = center_alignment
        head_style.borders = border

        data_style = XFStyle()
        data_style.alignment = center_alignment
        data_style.borders = border
        work_sheet = work_book.add_sheet("餐饮任务")
        limit = 10000
        count = self.get_data_scale(**kwargs)['count']
        times = (count + limit - 1) // limit
        add_header = False
        for i in range(times):
            kwargs["startIndex"] = i * limit + 1
            kwargs['endIndex'] = (i + 1) * limit + 1

            records = self.get_data(**kwargs)

            column_names = []
            y = 0
            for data in records:
                if not add_header:
                    x = 0
                    for column_name in data.keys():
                        work_sheet.write(y, x, column_name, head_style)
                        column_names.append(column_name)
                        x += 1
                    add_header = True
                    y += 1
                x = 0
                for column_name in column_names:
                    work_sheet.write(y, x, data[column_name], data_style)
                    x += 1
                y += 1
                x = 0

        work_book.save(BASE_WIN_OUTPUT_PATH + kwargs['table'] + ".xls")

    @staticmethod
    def get_cursor(**kwargs):
        # connection = pymysql.connect(host="10.128.62.33", usser="root", password="root", database="jy_catering")
        connection = pymysql.connect(host=kwargs['host'], user=kwargs['user'], password=kwargs['password'],
                                     database=kwargs['database'])
        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
        return cursor

    def get_data(self, **kwargs):
        cursor = self.get_cursor(**kwargs)
        sql = "select * from " + kwargs['table'] + ' limit ' + str(kwargs['startIndex']) + "," + str(
            kwargs['endIndex'])
        print(sql)
        cursor.execute(sql)
        return cursor.fetchall()

    def get_data_scale(self, **kwargs):
        cursor = self.get_cursor(**kwargs)
        sql = "select count(1) count from " + kwargs['table']
        cursor.execute(sql)
        return cursor.fetchone()

    def export(self):
        args = sys.argv[1:]
        opts, args = getopt.getopt(args, "hd:t:p:")
        props = {"profiles": "DEV"}
        for opt, arg in opts:
            if opt == '-h':
                print("python export_to_excel.py -d <database> -t <table> -p <profile> ")
                sys.exit(1)
            elif opt == '-d':
                props['database'] = arg
            elif opt == '-t':
                props['table'] = arg
            elif opt == '-p':
                props['profiles'] = arg
        profiles[props['profiles']]['database'] = props['database']
        profiles[props['profiles']]['table'] = props['table']

        self.export_to_csv(**profiles[props['profiles']])
