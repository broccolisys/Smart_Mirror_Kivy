from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from random import shuffle



Builder.load_string('''

#: import Button kivy.uix.button.Button

<MyScreenManager>:
    box2: box2
    Screen:
        name: "screen1"
        BoxLayout:
            orientation: "vertical"
            Button:
                text: "Button 1"
                on_release:
                    root.added_buttons.append(Button(text="Button 1"))
            Button:
                text: "Button 2"
                on_release:
                    root.added_buttons.append(Button(text="Button 2"))
            Button:
                text: "Button 3"
                on_release:
                    root.added_buttons.append(Button(text="Button 3"))
            Button:
                text: "Goto screen 2"
                on_release: root.current = "screen2"

    Screen:
        name: "screen2"
        on_enter: root.update_buttons()
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                orientation: "vertical"
                id: box2
            Button:
                text: "Goto screen 1"
                on_release:
                    root.current = "screen1"

''')



class MyScreenManager(ScreenManager):

    box2 = ObjectProperty(None)
    added_buttons = ListProperty([])


    def update_buttons(self,*args):

        self.box2.clear_widgets()
        shuffle(self.added_buttons)
        for i in self.added_buttons:
            self.box2.add_widget(i)
        self.added_buttons[:] = []



class MyApp(App):

    def build(self):

        return MyScreenManager()



MyApp().run()