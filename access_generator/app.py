from typing import List

import eel


def close_callback(route, websockets):
    if not websockets:
        exit()


@eel.expose
def get_class_list():
    form: str = '''
    <div>
        <input id="CustomClass" class="CustomClass" type="checkbox">CustomClass
        <input id="CustomClass_CREATE" class="CustomClass" type="checkbox">EntityOp.CREATE
        <input id="CustomClass_READ" class="CustomClass" type="checkbox">EntityOp.READ
        <input id="CustomClass_UPDATE" class="CustomClass" type="checkbox">EntityOp.UPDATE
        <input id="CustomClass_DELETE" class="CustomClass" type="checkbox">EntityOp.DELETE
    </div>
    '''
    return form


@eel.expose
def generate(data: List[str]) -> List[str]:
    for d in data:
        print(f"d: {d}")

    return ["result1", "result2", "result3", "result4"]


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(800, 600), port=31001, close_callback=close_callback)
