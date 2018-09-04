from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty, DictProperty
from datetime import datetime
from kivy.clock import Clock
import json
import urllib.request

apiUrl = 'http://api.openweathermap.org/data/2.5/forecast?q='
city = 'Daegu'
apikey = '&APPID=342f9ada733a2af5fc78bf8f074b0b1c'
weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = ['January','February','March','April','May','June','July','August'\
          ,'September','October','November','December']

class Weather(BoxLayout):
    city = StringProperty()
    temp = NumericProperty()
    temp_max = NumericProperty()
    temp_min = NumericProperty()
    condition = StringProperty()
    dateList = DictProperty()
    datePlusone = StringProperty()
    datePlustwo = StringProperty()
    datePlusthree = StringProperty()
    datePlusfour = StringProperty()
    datePlusfive = StringProperty()

    def weahter_update(self, *args):
        url = urllib.request.urlopen(apiUrl + city + apikey)
        apid = url.read()
        data = json.loads(apid.decode('utf-8'))

        self.city = data['city']['name']
        self.temp = data['list'][0]['main']['temp'] - 273.15
        self.temp_max = data['list'][0]['main']['temp_max'] - 273.15
        self.temp_min = data['list'][0]['main']['temp_min'] - 273.15
        self.condition = data['list'][0]['weather'][0]['main']
        self.dt = str(datetime.now())

        cnt = 0
        while cnt < 5:
            for nm in range(len(data['list'])):
                self.date = data['list'][nm]['dt_txt']
                if self.date[11:13] == '09':
                    if self.date[0:10] != self.dt[0:10]:
                        key = cnt
                        value = data['list'][nm]['weather'][0]['main']
                        self.dateList[key] = value
                        cnt += 1

        self.datePlusone = self.dateList[0]
        self.datePlustwo = self.dateList[1]
        self.datePlusthree = self.dateList[2]
        self.datePlusfour = self.dateList[3]
        self.datePlusfive = self.dateList[4]

        # json 파일 저장
        # with open('weather.json','w',encoding='utf-8') as make_file:
        # json.dump(data, make_file, ensure_ascii=False, indent="\t")

class WeatherApp(App):
    def build(self):
        weatherScreen= Weather()
        Clock.schedule_interval(weatherScreen.weahter_update, 3)
        return weatherScreen

if __name__ =='__main__':
    WeatherApp().run()