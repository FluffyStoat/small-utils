import os

import javalang
import eel

from typing import List, Dict
from javalang.tree import CompilationUnit
from os import walk, path


def close_callback(route, websockets):
    if not websockets:
        exit()


@eel.expose
def get_class_list():
    modifiers: List[str] = ["private", "static", "final"]

    (dir_path, dir_names, file_names) = next(walk("./test/sales/entity/"))

    cls: Dict[str, List[str]] = {}

    for file_name in file_names:
        file_path: str = dir_path + path.sep + file_name
        filename, file_extension = os.path.splitext(file_path)

        if file_extension == ".java":
            with open(file_path, "r") as f:
                data: str = f.read()

                print(f"file_name: {file_name}")

                tree: CompilationUnit = javalang.parse.parse(data)
                cls_name: str = tree.types[0].name
                cls[cls_name] = []
                print(f"class: {cls_name}")

                for field in tree.types[0].fields:
                    if set(field.modifiers) != set(modifiers):
                        name: str = field.declarators[0].name
                        cls[cls_name].append(name)
                        print(f"field: {name}")

    # return cls
    return ["Driver", "Customer", "Order", "Account", "Building", "MasterRequest"]


@eel.expose
def generate(values: List[str]) -> List[str]:
    for val in values:
        print(f"val: {val}")

    return ["result1", "result2", "result3", "result4"]


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(800, 600), port=31001, close_callback=close_callback)
