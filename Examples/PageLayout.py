# Creating a PageLayout example


from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""
PageLayout:
    Button:
        text:'Page1'
    Button:
        text:'Page2'
    Button:
        text:'Page3'                                
                                
                                
                                """))
