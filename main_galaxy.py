from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    line = None

    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        # print(f"INIT Width: {str(self.width)}, INIT Height: {str(self.height)}")

    def on_parent(self, widget, parent):
        pass

    def on_size(self, *args):
        print(f"INIT Width: {str(self.width)}, INIT Height: {str(self.height)}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height*.75
        self.update_vertical_lines()

    def on_perspective_point_x(self,widget,value):
        # print(f"PERSPECTIVE X: {str(value)}")
        pass

    def on_perspective_point_y(self,widget,value):
        # print(f"PERSPECTIVE Y: {str(value)}")
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            self.line = Line(points=[100,0,100,100])

    def update_vertical_lines(self):
        center_x = int(self.width/2)
        #center_y = int(self.height*.75)
        self.line.points = [center_x,0,center_x,100]


class GalaxyApp(App):
    pass


GalaxyApp().run()