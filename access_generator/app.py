from typing import List

import eel


def close_callback(route, websockets):
    if not websockets:
        exit()


@eel.expose
def get_class_list():
    form: str = '''
    <table>
      <tr>
        <td>
            <div class="checkbox">
                <input class="custom-checkbox CustomClass" type="checkbox" id="cls" name="cls" value="class">
                <label for="cls">CustomClass</label>
            </div>
        </td>
        <td>
            <div class="checkbox">
                <input class="custom-checkbox CustomClass" type="checkbox" id="create" name="create" value="create">
                <label for="create">CREATE</label>
            </div>
        </td>
        <td>
            <div class="checkbox">
                <input class="custom-checkbox CustomClass" type="checkbox" id="read" name="read" value="read">
                <label for="read">READ</label>
            </div>
        </td>
        <td>
            <div class="checkbox">
                <input class="custom-checkbox CustomClass" type="checkbox" id="update" name="update" value="update">
                <label for="update">UPDATE</label>
            </div>
        </td>
        <td>
            <div class="checkbox">
                <input class="custom-checkbox CustomClass" type="checkbox" id="delete" name="delete" value="delete">
                <label for="delete">DELETE</label>
            </div>
        </td>
      </tr>
    </table>
    '''
    return form


@eel.expose
def generate(data: List[str]) -> List[str]:
    for d in data:
        print(f"d: {d}")

    return ["result1", "result2", "result3", "result4"]


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(1080, 1024), port=31001, close_callback=close_callback)
