from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Line, Ellipse, Color
import random
from kivy.core.window import Window

frme = ''
www = 2

class Main(Widget):
    def clearer(self, *args):
        global frme
        try:
            frme.canvas.clear()
        except:
            pass

    def update(self, *args):
        ww = self.ids['widh']
        wtxt = ww.text
        if len(wtxt) > 2:
            ww.text = wtxt[:2]
        global www
        try:
            www = float(ww.text)
        except:
            ww.text = ''
            www = 1

class Frame(Widget):
    def on_touch_down(self, touch):
        global frme, www
        frme = self
        with self.canvas:
            d = 40
            pos_x = touch.x - (d/2)
            pos_y = touch.y - (d/2)
            Color(1, 1, 1, 1)
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = www)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


Builder.load_string('''
<Main>
    FloatLayout:
        Frame:
        Button:
            text: 'Clear'
            color: 0, 1, 1, 1
            on_release: app.root.clearer()
            size_hint: None, None
            font_size: 20
            size: 60 ,25
            pos: 10, 10

        TextInput:
            text: '2'
            on_text: root.update()
            size_hint: None, None
            id: widh
            size: 30, 30
            pos: root.width - self.width - 10, 10

        Label:
            size_hint: None, None
            size: self.texture_size
            text: 'Width: '
            pos: root.width - self.width - widh.width - 13, 13

''')

class MainApp(App):
    def build(self):
        self.instance = Frame()
        return Main()

if __name__ == '__main__':
    MainApp().run()
