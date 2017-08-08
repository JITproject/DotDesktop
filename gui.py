from Tkinter import *
import Image

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
			
    def createfile(self):
		self.DotDesktop = open(self.name.get() + ".desktop",'w')
    
    def createWidgets(self):
		
        #App icon
        #self.iconlabel = Label(self, text = "Icon Route")        
        #self.iconlabel.grid(row=0,column=1)
        self.iconroute = Entry(self)
        self.iconroute.insert(END, 'icon route')
        self.iconroute.grid(row=0,column=1)
        
        #App name
        self.name = Entry(self)
        self.name.insert(END, 'Name')
        self.name.grid(row=0, column = 0)
        
        #Type
        self.typelabel = Label(self, text = "Type")        
        self.typelabel.grid(row=2,column=0)
        self.application = Entry(self)
        self.application.insert(END, 'Application')
        self.application.grid(row=2,column=1)
        
        #Path
        self.pathlabel = Label(self, text = "Application Path")
        self.pathlabel.grid(row = 1, column = 0)
        self.path = Entry(self)
        self.path.insert(END, '/opt/')        
        self.path.grid(row=1,column=1)
        
        #Categories
        self.catlabel = Label(self, text = "Categories")
        self.catlabel.grid(row =3, column=0)
        categories = ("Education","Languages","Java", "Network", "Accesories") # change for a text file later
        self.catselector = Spinbox(self, values = categories) 
        self.catselector.grid(row=3,column=1)
        self.allcats = Text(self, height = 3, width = 15) #the categories chosen in the spiner go here
        self.allcats.grid(row=4,column=1)
        
        #terminal?
        self.trmyesno = Label(self, text = "Run on a Terminal?")
        self.trmyesno.grid(row=5,column=0)
        self.terminal = Button(self, text = 'true', relief='raised')
        #self.terminal["command"] = self.TerminalToggle
        self.terminal.grid(row=6,column=0)
        
        #startupnotify?
        self.startnotif = Label(self, text = "Startup Notify?")
        self.startnotif.grid(row=5,column=1)
        self.startup = Button(self, text = 'true', relief='raised')
        #self.startup["command"] = self.StartupToggle
        self.startup.grid(row=6,column=1)
        
        #Quit Button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=15,column=1)
        
        #create button
        self.create = Button(self)
        self.create["text"] = "Create .desktop"
        self.create["fg"]   = "green"
        self.create["command"] =  self.createfile
        self.create.grid(row=15,column=0)
        
	
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
