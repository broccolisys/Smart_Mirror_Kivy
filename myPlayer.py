import webbrowser

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class myPlayer(BoxLayout):


class myPlayerApp(App):
    def build(self):
        return myPlayer()

if __name__ == '__main__':
    myPlayerApp().run()

