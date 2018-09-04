from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.app import App
from datetime import datetime
from kivy.clock import Clock
import json
import urllib.request
from pprint import pprint

apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q='
city = 'Daegu'
apikey = '&APPID=342f9ada733a2af5fc78bf8f074b0b1c'
weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = ['January','February','March','April','May','June','July','August'\
          ,'September','October','November','December']

class WaitScreen(RelativeLayout):
    uxTime = StringProperty('')
    uxWeeksDayMonths = StringProperty('')
    cityWeatherTemp = StringProperty('')

    def time_update(self, *args):
        today = datetime.now()
        self.uxWeeksDayMonths = weekday[today.weekday()] + ', ' + str(today.day) + ', ' +  (months[today.month - 1])
        self.uxTime = str(today.strftime('%H:%M:%S'))

    def weahter_update(self, *args):
        url = urllib.request.urlopen(apiUrl + city + apikey)
        apid = url.read()
        data = json.loads(apid.decode('utf-8'))
        pprint(data)
        self.cityWeatherTemp = data['name'] + ' ' +  data['weather'][0]['main'] + '  ' + str(data['main']['temp'] - 273.15) + '˚C'


class WaitScreenApp(App):
    def build(self):
        waitTimeScreen = WaitScreen()
        Clock.schedule_interval(waitTimeScreen.time_update, 1)
        Clock.schedule_interval(waitTimeScreen.weahter_update, 1)
        return waitTimeScreen

if __name__ =='__main__':
    WaitScreenApp().run()