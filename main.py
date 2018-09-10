from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from datetime import datetime
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
Builder.load_file('main.kv')

weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

class IconButton(ButtonBehavior, Image):
    pass

class MyMain(BoxLayout):
    uxTime = StringProperty('')
    uxWeeksDayMonths = StringProperty('')

    def time_update(self, *args):
        today = datetime.now()
        self.uxWeeksDayMonths = weekday[today.weekday()] + '/' + str(today.day) + '/' + str(today.month)
        self.uxTime = str(today.strftime('%H:%M:%S'))

class MyMainApp(App):
    def build(self):
        MyMainScreen = MyMain()
        Clock.schedule_interval(MyMainScreen.time_update, 1)
        return MyMainScreen

if __name__ == '__main__':
    MyMainApp().run()

