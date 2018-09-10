
from kivy.app import App
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.logger import Logger
from kivy.lang import Builder

# We first define our GUI
kv = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'Configure app (or press F1)'
        on_release: app.open_settings()
'''

json = '''
[
    {
        "type": "string",
        "title": "Label caption",
        "desc": "Choose the text that appears in the label",
        "section": "My Label",
        "key": "text"
    },
    {
        "type": "numeric",
        "title": "Label font size",
        "desc": "Choose the font size the label",
        "section": "My Label",
        "key": "font_size"
    },
     {
        "type": "string",
        "title": "City of the weather",
        "desc": "Choose the city of the weather",
        "section": "My Label",
        "key": "city_weather"
    }
]
'''


class MyApp(App):
    def build(self):
        self.settings_cls = MySettingsWithTabbedPanel
        self.use_kivy_settings = False
        root = Builder.load_string(kv)
        return root

    def build_config(self, config):
        # config 기본 설정
        config.setdefaults('My Label', {'text': 'Hello', 'font_size': 20,"city_weather":'Daegu'})

    def build_settings(self, settings):
        # json 에 저장
        settings.add_json_panel('My Label', self.config, data=json)

    def on_config_change(self, config, section, key, value):

        # value 변경
        Logger.info("main.py: App.on_config_change: {0}, {1}, {2}, {3}".format(
            config, section, key, value))

        if section == "My Label":
            if key == "text":
                self.root.ids.label.text = value
            elif key == "font_size":
                self.root.ids.label.font_size = float(value)
            elif key == "city_weather":
                self.root.ids.label.city_weather = value

    def close_settings(self, settings=None):
        Logger.info("main.py: App.close_settings: {0}".format(settings))
        super(MyApp, self).close_settings(settings)


class MySettingsWithTabbedPanel(SettingsWithTabbedPanel):
    """
    It is not usually necessary to create subclass of a settings panel. There
    are many built-in types that you can use out of the box
    (SettingsWithSidebar, SettingsWithSpinner etc.).

    You would only want to create a Settings subclass like this if you want to
    change the behavior or appearance of an existing Settings class.
    """
    def on_close(self):
        Logger.info("main.py: MySettingsWithTabbedPanel.on_close")

    def on_config_change(self, config, section, key, value):
        Logger.info(
            "main.py: MySettingsWithTabbedPanel.on_config_change: "
            "{0}, {1}, {2}, {3}".format(config, section, key, value))


MyApp().run()
