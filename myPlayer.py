import webbrowser

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class myPlayer(BoxLayout):
    search_input = ObjectProperty()
    def youtube_search(self):
        search = self.search_input.text
        webbrowser.open('https://www.youtube.com/results?search_query='+search)

class myPlayerApp(App):
    def build(self):
        return myPlayer()

if __name__ == '__main__':
    myPlayerApp().run()

