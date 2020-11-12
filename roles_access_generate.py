#!/usr/bin/python

# Script for generation EntityAccess and EntityAttributeAccess for files
# @EntityAccess(entityClass=<name>.class,
#   operations = {EntityOp.CREATE, EntityOp.READ, EntityOp.UPDATE, EntityOp.DELETE})
# @EntityAttributeAccess(entityClass = BusinessUser.class, modify = "*")

import getopt
import sys
import mmap
import re

from os import walk, path
from typing import List

# Todo: Add operations type, refactor code, split by functions


def main(argv: List[str]):
    input_dir = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hd:o:", ["dir=", "ofile="])
    except getopt.GetoptError:
        print('roles_access_generate.py -d <dir> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('roles_access_generate.py -d <dir> -o <outputfile>')
            sys.exit()
        elif opt in ("-d", "--dir"):
            input_dir = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    if input_dir == '' or output_file == '':
        print('roles_access_generate.py -d <dir> -o <outputfile>')
    else:
        print(f'Input directory: {input_dir}')
        print(f'Output file: {output_file}')

        (dir_path, dir_names, file_names) = next(walk(input_dir))

        print(f"{dir_path}")
        print(f"{dir_names}")
        print(f"{file_names}")

        class_names: List[str] = []

        for file_name in file_names:
            with open(dir_path + path.sep + file_name, 'rb', 0)\
                    as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                result = re.search(rb'class\s([A-z]+)\s', s)
                if result is not None:
                    class_names.append(result.group(1).decode("utf-8"))

        with open(output_file, "w") as result_file:
            for cls_name in class_names:
                rec: str = f'@EntityAccess(entityClass={cls_name}.class, ' \
                           f'operations = {{EntityOp.CREATE, EntityOp.READ, EntityOp.UPDATE, EntityOp.DELETE}})\n'
                result_file.write(rec)
                print(rec)

            result_file.write("\n")

            for cls_name in class_names:
                rec = f'@EntityAttributeAccess(entityClass = {cls_name}.class, modify = "*")\n'
                result_file.write(rec)
                print(rec)


if __name__ == '__main__':
    main(sys.argv[1:])

