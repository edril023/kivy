from kivy.app import App
from kivy.uix.button  import Button

class myApp (App):
    def build(self):
        return Button(text = "Hello world! this is my frist program in kivi \n I'm a SESIANO A student, and I hate my teacher"
        )
if __name__ == "__main__":
    myApp().run()