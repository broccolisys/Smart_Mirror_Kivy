from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class myPlayer(BoxLayout):
    pass

class myPlayerApp(App):
    def build(self):
        return myPlayer()

if __name__ == '__main__':
    myPlayerApp().run()

