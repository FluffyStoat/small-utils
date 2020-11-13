from typing import List

import eel


def close_callback(route, websockets):
    if not websockets:
        exit()


@eel.expose
def get_class_list():
    return ["Driver", "Customer", "Order", "Account", "Building", "MasterRequest"]


@eel.expose
def generate(data: List[str]) -> List[str]:
    for d in data:
        print(f"d: {d}")

    return ["result1", "result2", "result3", "result4"]


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(1080, 1024), port=31001, close_callback=close_callback)
