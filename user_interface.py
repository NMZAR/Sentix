
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import Button, GridLayout






class MainApp(App):

    def build (self):


        Layout = GridLayout(cols=2)
        self.type = TextInput (text = "enter")
        submit = Button(text = 'Submit' , on_press= self.submit)

        Layout.add_widget =(self.type)
        Layout.add_widget.add_widget(submit)


        return Layout



    def submit(self, obj):
        print("type: " + self.type.text)

MainApp().run()





