# -*- coding: utf-8 -*-
import random
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kivy.require('2.1.0')


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.layout = BoxLayout(orientation='vertical')
        self.lines = open("words.txt", "r").readlines()
        self.rdm = self.lines[random.randint(0, len(self.lines) - 1)].split("=")

        self.text = Label(text=self.rdm[0])
        self.field = TextInput()
        self.button = Button(text="Suivant")

    def changeText(self, *args):
        print(self.rdm[1] == self.field.text, self.rdm, self.field.text)
        if self.rdm[1].replace("\r", "").replace("\n", "") == self.field.text.replace("\r", "").replace("\n", ""):
            self.rdm = self.lines[random.randint(0, len(self.lines) - 1)].split("=")
            self.text.text = self.rdm[0]

    def build(self):
        self.button.bind(on_press=self.changeText)

        self.layout.add_widget(self.text)
        self.layout.add_widget(self.field)
        self.layout.add_widget(self.button)

        return self.layout


if __name__ == '__main__':
    MyApp().run()
