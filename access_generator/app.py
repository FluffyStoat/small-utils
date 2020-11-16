import os
from os import walk, path
from typing import List, Dict

import javalang
import kivy
from javalang.tree import CompilationUnit
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

kivy.require('2.0.0')  # replace with your current kivy version !


def close_callback(route, websockets):
    if not websockets:
        exit()


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


def on_checkbox_active(checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)
        self.cols = 1
        self.rows = 1

        for cls in get_class_list():

            row_layout: BoxLayout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
            layout.add_widget(row_layout)

            class_layout: BoxLayout = BoxLayout(orientation='horizontal')

            check_box: CheckBox = CheckBox()
            check_box.color = [255, 250, 250, 1]

            class_layout.add_widget(check_box)
            class_layout.add_widget(Label(text=f'[b]{cls}[/b]', markup=True))
            row_layout.add_widget(class_layout)

            operations: List[str] = ['Создать', 'Просмотр', 'Редактировать', 'Удалить']

            for oper in operations:
                operations_layout = BoxLayout(orientation='horizontal')

                check_box: CheckBox = CheckBox()
                check_box.color = [255, 250, 250, 1]
                check_box.bind(active=on_checkbox_active)

                operations_layout.add_widget(check_box)
                operations_layout.add_widget(Label(text=f"{oper}"))
                row_layout.add_widget(operations_layout)


class GeneratorApp(App):
    @staticmethod
    def build():
        return MainScreen()


if __name__ == '__main__':
    GeneratorApp().run()
