__author__ = 'sepulvedaavila'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

#this 'imports' the styles defined in the .kv file
Builder.load_file("Form.kv")

#this creates the Screen Manager object
screens = ScreenManager(transition = NoTransition())

#this is a Screen class that contains all the functions required
#by the screen
class Calc(Screen):

        #arithmethic functions are the only ones non-class
	def suma(a,b):
		return a+b 

	def resta(a,b):
		return a-b 

	def multi(a,b):
		return a*b

	def divis(a,b):
                #this 'catches' the indetermination
                #of a division
		if b == 0:
			return None
		else:
			return a/b
        
        #this is a map for the functions...
        #...and provides agile access to them
	functions_map = {
                0: divis,
                1: multi,
                2: resta,
                3: suma
                }

        #these are our operational variables
	a = 0
	b = 0
	result = 0

        #this var is to be filled by the selected arith function
	opt_selected = None

	def operation(self, op_id):
                #verifies if there is some content in the input
		if self.ids["text_input"].text:
                        #verifies if the content isn't only a dot
			if self.ids["text_input"].text != '.':
                                #all cleared, we can parse the content into a float
				self.a = float(self.ids["text_input"].text)
                                
                                #and we put the 'partial result' into the hint text of the input
				self.ids["text_input"].hint_text = str(self.a)

                                #and this clears the text itself so that we can only see the hint
				self.ids["text_input"].text = ""

                                #now we assign the function selected into our var, it is an int
				self.opt_selected = op_id

                                #and we set the focus on the text input so that we can write in it
				self.ids["text_input"].focus = True

	def showResult(self):
            #verifies that there's actual content
            if self.ids["text_input"].text:
                #verifies that the content isn't only a dot
		if self.ids["text_input"].text != '.':

                        #all cleared and set we can parse the content into a float
			self.b = float(self.ids["text_input"].text)

                        #and we can get the result by accessing our functions map and immediatly...
                        #...passing the params
			self.result = self.functions_map[self.opt_selected](self.a, self.b)
                        
                        #if the exception caught by the division function yields None...
                        #...we have to clear all the vars and display the actual error
                        if self.result == None:
                            self.a = 0
                            self.b = 0
                            self.result = 0
                            self.ids["text_input"].text = "" #clears the input

                            #we set the hint text with the error message
                            self.ids["text_input"].hint_text = "Error: Indetermination"
                            #and now we set the input focus to false
                            self.ids["text_input"].focus = False

                        #otherwise we have to display the result properly...
                        #...in text so that our next operation can be... 
                        #...appendable with the current result
                        else:
                            self.ids["text_input"].text = str(self.result)
			    self.ids["text_input"].focus = False
        
        #this appends text to the current input
	def addToText(self, b):
            self.ids["text_input"].text += b

	#this function clears all the vars and input
        def clearText(self):
		self.ids["text_input"].text = ""
		self.a = 0
		self.b = 0
		self.ids["text_input"].hint_text = ""
	pass

#this add the Calc screen to the Screen Manager
screens.add_widget(Calc(name='calc'))

#this is the App class that launches the Screen Manager
class Calculadora(App):
        #if we wanted, we could set more functions here
        #and these can be accessed from the .kv file
	def build(self):
            return screens 

#the actual launcher of the app
#this checks for the file to be the main file for the project
#it refrains everything from running as a 'script' or something
if __name__ == '__main__':
	Calculadora().run()
