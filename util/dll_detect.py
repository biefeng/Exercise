# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/06/16 11:36
# file_name : dll_detect.py.py

import os


def del_excess_dll():
    for root, sub_dirs, sub_files in os.walk("E:\\workspace\\idea\\print-service\\jre1.8.0_162\\bin"):
        if root == "E:\\workspace\\idea\\print-service\\jre1.8.0_162\\bin":
            for sub_file in sub_files:
                if sub_file.find('.dll') <= 0:
                    continue
                dll_file_name = os.path.join(root, sub_file)
                with open("C:\\Users\\33504\\dll.txt") as dll_txt:
                    line = dll_txt.readline()
                    # dlls = line.split(",")
                    # print(len(dlls))
                    # for dll in dlls:
                    if line.find(sub_file) > 0:
                        print(sub_file)
                    else:
                        try:
                            os.remove(dll_file_name)
                        except Exception as e:
                            print(e)


def find_class():
    classes = set()
    count = 0
    with open("E:\\workspace\\idea\\print-service\\loaded_class.txt") as loaded_class:
        for line in loaded_class.readlines():
            if line.find(".jar") > 0:
                count += 1
                import re
                findall = re.findall(".*[/\\\\](\S+)\s*\\]", line)
                if line.find('Loaded') > 0 and findall[0] == 'rt.jar':
                    class_name = re.findall("\\[Loaded\s(\S+)\s.*", line)[0]
                    # if class_name.rfind("$") > 0:
                    #     class_name = class_name[:class_name.rfind("$")]
                    print(class_name)
                    # print(class_name)
                    cop_file(class_name)
                classes.add(findall[0])

    print(count)
    print(classes)


def cop_file(filename):
    dirs = filename
    import shutil, os
    base_src = "E:\\workspace\\idea\\print-service\\jre1.8.0_162\\lib\\rt\\"
    base_dest = "E:\\workspace\\idea\\print-service\\jre1.8.0_162\\lib\\tmp\\"
    filename = filename.replace(".", "\\") + ".class"
    dirs = dirs[:dirs.rfind(".")].replace(".", "\\")
    os.makedirs(base_dest + dirs, exist_ok=True)
    try:
        src_filename = base_src + filename
        print(src_filename)
        shutil.copyfile(src_filename, base_dest + filename)
    except Exception as e:
        print(e)


def find_class_for_exe4j():
    import re
    with open("E:\\workspace\\idea\\print-service\\loaded_class_for_exe4f.txt") as loaded:
        for line in loaded.readlines():
            findall = re.findall("import\s+(\S+);", line)
            # if line.find("$") > 0:
            #     findall = re.findall("import\s(\S+?)\$.*?;", line)
            if len(findall) > 0:
                cop_file(findall[0])


if __name__ == '__main__':
    # find_class()
    find_class_for_exe4j()
