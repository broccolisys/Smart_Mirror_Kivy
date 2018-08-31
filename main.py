from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget


runTouchApp(Builder.load_string(




    '''

RelativeLayout:
    
    padding: 10
    Button:
        text: 'R1'
        size_hint: .2, .2
        pos: 30, 50
    Button:
        text: 'R2'
        size_hint: .2 ,.2
        pos: 100, 300
    Button:
        text: 'R3'
        size_hint: .2 ,.2
        pos: 200, 200
    Button:
        text: 'R4'
        size_hint: .2 ,.2
        pos: 300, 100

'''))


if __name__ == '__main__':
    MyPaintApp().run()