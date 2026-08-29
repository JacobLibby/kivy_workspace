from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout

class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):

    pass

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0,100):
            #size = dp(100)
            #b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            b = Button(text=str(i+1),size_hint=(1,None),size=(1,dp(100)))
            self.add_widget(b)

    pass


class GridLayoutInfoList(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        for i in range(0,100):
            size = dp(100)
            b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)

    pass


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass





class BoxLayoutExample(BoxLayout):

    """    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""
    pass


class MainWidget(Widget):
    pass

# need to have "App" suffix AND reference
class TheLabApp(App):
    pass

TheLabApp().run()

