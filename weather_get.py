from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty, DictProperty
from datetime import datetime
from kivy.clock import Clock
import json
import urllib.request
from pprint import pprint


class Weather(BoxLayout):
    pass


class WeatherApp(App):
    def build(self):
        weatherScreen= Weather()
        return weatherScreen

if __name__ =='__main__':
    WeatherApp().run()