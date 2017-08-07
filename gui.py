from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
    
	def TerminalToggle(self):
		if (self.terminal('relief')[-1] == 'sunken'):
			self.terminal(relief='sunken')
		else:
			self.terminal(relief='sunken')
			
	def StartupToggle(self):
		if (self.snotifstate('relief')[-1] == 'sunken'):
			self.snotifstate(relief='raised')
		else:
			self.snotifstate(relief='sunken')
    
    def createWidgets(self):
		#Quit Button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=5,column=1)
        
        #create button
        self.create = Button(self)
        self.create["text"] = "Create .desktop"
        self.create["fg"]   = "green"
        self.create.grid(row=5,column=0)
        
        #App name
        self.name = Entry(self)
        self.name.insert(END, 'Name')
        self.name.grid(row=0, column = 0)
        
        #Type
        self.typelabel = Label(self, text = "Type")        
        self.application = Entry(self)
        self.application.insert(END, 'Application')
        self.application.grid(row=2,column=1)
        self.typelabel.grid(row=2,column=0)
        
        #Path
        self.typelabel = Label(self, text = "Application Path")
        self.path = Entry(self)
        self.application.insert(END, '/opt/')
        self.typelabel.grid(row = 1, column = 0)
        self.path.grid(row=1,column=1)
        
        #Categories
        self.typelabel = Label(self, textvariable = "Categories")
        categories = ("Education","Languages","Java", "Network", "Accesories") # change for a text file later
        self.catselector = Spinbox(self, values = categories) 
        self.allcats = Text(self, height = 3, width = 15) #the categories chosen in the spiner go here
        
        #terminal?
        self.trmyesno = Label(self, text = "Run on a Terminal?")
        self.terminal = Button(self, text = 'yes', relief='raised')
        #self.terminal["command"] = self.TerminalToggle
        
        #startupnotify?
        self.startnotif = Label(self, text = "Startup Notify?")
        self.startup = Button(self, text = 'yes', relief='raised')
        #self.startup["command"] = self.StartupToggle
        
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
