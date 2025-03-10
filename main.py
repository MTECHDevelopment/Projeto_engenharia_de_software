from kivy.app import app

from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
