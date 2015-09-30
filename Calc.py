#__author__ == 'sepulvedaavila'

import sys

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


Builder.load_file("Form.kv")

screens = ScreenManager(transition =NoTransition())


class Calc(Screen):

	def suma(a,b):
		return a+b

	def resta(a,b):
		return a-b

	def multi(a,b):
		return a*b

	def divis(a,b):
		if b == 0:
			return "Error: Indetermination"
		else:
			return a/b

	options= {0: divis,1: multi,2: resta,3: suma}
	a = 0
	b = 0
	result = 0
	opt_selected = None

	def operation(self, op_id):
		if self.ids["text_input"].text:
			if self.ids["text_input"].text != '.':
				self.a = float(self.ids["text_input"].text)
				self.ids["text_input"].hint_text = str(self.a)
				self.ids["text_input"].text = ""
				self.opt_selected = op_id
				self.ids["text_input"].focus = True

	def showResult(self):
		if self.ids["text_input"].text != '.':
			self.b = float(self.ids["text_input"].text)
			self.result = self.options[self.opt_selected](self.a, self.b)
			self.ids["text_input"].text = str(self.result)
			self.ids["text_input"].focus = False

	def addToText(self, b):
		self.ids["text_input"].text += b
	def clearText(self):
		self.ids["text_input"].text = ""
		self.a = 0
		self.b = 0
		self.ids["text_input"].hint_text = ""
	pass

screens.add_widget(Calc(name='calc'))

class Calculadora(App):

	def build(self):
		myCalc = Calc()
		return myCalc

if __name__ == '__main__':
	Calculadora().run()