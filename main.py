from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
#
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.textinput import TextInput


class Menu(Screen):
    pass


class Person(GridLayout, Screen):

    # tu kopiuje
    container = ObjectProperty(None)
    data_list = ListProperty([])

    # zbieranie listy z inputow
    def save_data(self):
        for child in reversed(self.container.children):
            if isinstance(child, TextInput):
                self.data_list.append(child.text)

        print(self.data_list)


class Creator(GridLayout, Screen):
    list_of_documents = []

    # detain
    def checkbox_handle(self, instance, value, name):
        if value:
            self.list_of_documents.append(name)
        else:
            self.list_of_documents.remove(name)

        print(self.list_of_documents)


# Load GUI with screen change
GUI = Builder.load_file("main.kv")


class main(App):

    def build(self):
        return GUI  # Menu()

    def change_screen(self, screen_name):
        # Get the screen manager from kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name



main().run()
