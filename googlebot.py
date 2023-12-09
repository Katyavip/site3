from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout


class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula
    def add_num(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()
    def operation(self, instance):
        if (str(instance.text).lower() == "x"):
            self.formula += "*"
        elif (str(instance.text).lower() == "c"):
            self.formula = "0"
        else:
            self.formula += str(instance.text)
        self.update_label()
    def result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        if self.lbl.text[-1] == "0":
            f = self.lbl.text.find(".")
            self.lbl.text = self.lbl.text[:f]
        self.formula = "0"
    def el(self, instance):
        self.formula = "0"
        self.lbl.text = "0"
    def el2(self, instance):
        self.lbl.text = self.lbl.text[0:len(self.lbl.text) - 1]
        self.formula = str(self.lbl.text)
    def percent(self, instance):
        op = ["*", "÷", "+", "-"]  
        stroka = ""
        self.lbl.text = self.lbl.text   
        if len(self.lbl.text) == 1:   
            stroka += self.lbl.text
            self.lbl.text = ""
        else:
            while self.lbl.text[-1]  not in op:
                stroka += self.lbl.text[-1]
                self.lbl.text = self.lbl.text[0:len(self.lbl.text) - 1]
        stroka = ''.join(reversed(stroka))
        stroka = int(stroka)/100
        self.formula = str(self.lbl.text)
        self.formula += str(stroka)
        self.lbl.text += str(stroka)
        stroka = ""
    def delenie(self, instance):
        self.formula += str("/")
        self.lbl.text += "/"
    
    def el3(self, instance):
        op = ["*", "÷", "+", "-"]

        for i in op:
            if i in self.lbl.text:
                while self.lbl.text[-1] not in op:
                    self.lbl.text = self.lbl.text[0:len(self.lbl.text) - 1]
            else:
                self.lbl.text = "0"

        self.formula = str(self.lbl.text)
        
    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=5)
        gl = GridLayout(cols=4, spacing=2, size_hint=(1, .6))

        al = AnchorLayout(anchor_x='right', anchor_y='center', size_hint=(1, .5))
        self.lbl = Label(text='0', font_size=40, halign="right", valign="top", text_size=(400 - 15, 600 * .2 - 5))
        al.add_widget(self.lbl)
        bl.add_widget(al)

        gl.add_widget(Button(text='%', font_size=20, on_press=self.percent))
        gl.add_widget(Button(text='CE', font_size=20, on_press=self.el3))
        gl.add_widget(Button(text='C', font_size=20, on_press=self.el))
        gl.add_widget(Button(text='<=', font_size=20, on_press=self.el2))

        gl.add_widget(Button(text='7', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='8', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='9', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='X', font_size=20, on_press=self.operation))

        gl.add_widget(Button(text='4', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='5', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='6', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='-', font_size=20, on_press=self.operation))

        gl.add_widget(Button(text='1', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='2', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='3', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='+', font_size=20, on_press=self.operation))

        gl.add_widget(Button(text='0', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='.', font_size=20, on_press=self.add_num))
        gl.add_widget(Button(text='÷', font_size=20, on_press=self.delenie))
        gl.add_widget(Button(text='=', font_size=20, on_press=self.result))

        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    CalculatorApp().run()  # запуск приложения калькулятора