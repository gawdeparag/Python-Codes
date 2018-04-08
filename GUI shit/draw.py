from tkinter import *
from random import randint
#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/
class Application(Frame):
     
    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.toolsThickness = 2
        self.rgb = "#%02x%02x%02x" % (255, 255, 255)
         
        self.pack()
        self.createWidgets()
         
        master.bind('a', self.thicknessPlus)
        master.bind('s', self.thicknessMinus)
 
         
    def createWidgets(self):
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)        
         
        self.leftFrame = Frame(self, bg = tk_rgb)
        self.leftFrame.pack(side = LEFT, fill = Y)
         
        self.label = Label(self.leftFrame, text = "choose a RGB color: ")
        self.label.grid(row = 0, column = 0, sticky = NW, pady = 2, padx = 3)
        #-----------------------------------------------
        self.entryFrame = Frame(self.leftFrame)
        self.entryFrame.grid(row = 1, column = 0,
                              sticky = NW, pady = 2, padx = 3)
         
        self.myEntry1 = Entry(self.entryFrame, width = 5, insertwidth = 3)
        self.myEntry1.pack(side = LEFT, pady = 2, padx = 4)
         
        self.myEntry2 = Entry(self.entryFrame, width = 5)
        self.myEntry2.pack(side = LEFT, pady = 2, padx =4)
         
        self.myEntry3 = Entry(self.entryFrame, width = 5)
        self.myEntry3.pack(side = LEFT, pady = 2, padx = 4)
        #----------------------------------------------
        self.bttn1 = Button(self.leftFrame,
                             text = "accept", command = self.setColor)
        self.bttn1.grid(row = 2, column = 0, pady = 2, padx = 3, sticky = NW)
         
        self.labelThickness = Label(
                            self.leftFrame,
                            text = "drawing tools' thickness:")
        self.labelThickness.grid(row = 3,
                                 column = 0, pady = 2, padx = 3)
         
        self.myScale = Scale(
                            self.leftFrame, from_ = 1, to = 25,
                            orient = HORIZONTAL,
                            command = self.setThickness
                            )
        self.myScale.set(2)
        self.toolsThickness = 2
        self.myScale.grid(
                          row = 4, column = 0,
                          pady = 2, padx = 3, sticky = S,
                          )
         
        self.labelTools = Label(
                                self.leftFrame,
                                text = "chose a drawing tool:",
                                )
        self.labelTools.grid(
                             row = 5, column = 0,
                             pady = 2, padx = 3,
                             sticky = NW
                             )
         
        Radiobutton(self.leftFrame,
                    text = "line",
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = 3, pady = 2,
                                    row = 6, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftFrame,
                    text = "line2",
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = 3, pady = 2,
                                    row = 7, column = 0,
                                    sticky = NW
                                    )
 
        Radiobutton(self.leftFrame,
                    text = "flowers tool",
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = 3, pady = 2,
                                    row = 8, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftFrame,
                    text = "spray",
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = 3, pady = 2,
                                    row = 9, column = 0,
                                    sticky = NW,
                                    )
        Radiobutton(self.leftFrame,
                    text = "cosmos",
                    variable = self.radiobuttonValue,
                    value = 5).grid(padx = 3, pady = 2,
                                    row = 10, column = 0,
                                    sticky = NW,
                                    )
                     
        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.delteAll)
        self.buttonDeleteAll.grid(padx = 3, pady = 2,
                                    row = 11, column = 0,
                                    sticky = NW)
#----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width = 800,
                                height = 500, relief=RAISED, borderwidth=5)
        self.myCanvas.pack(side = RIGHT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)
         
#----------------------------------------------------------------------
    def setThickness(self, event):      
        print(self.myScale.get())
        self.toolsThickness = self.myScale.get()
         
    def setColor(self):
        try:
            val1 = int(self.myEntry1.get())
            val2 = int(self.myEntry2.get())
            val3 = int(self.myEntry3.get())
            if 0 <=(val1 and val2 and val3) <= 255:              
                self.rgb = "#%02x%02x%02x" % (val1, val2, val3)
            self.myEntry1.delete(0, END)
            self.myEntry2.delete(0, END)
            self.myEntry3.delete(0, END)
         
        except ValueError:
            print("That's not an int!")
        # set focus to something else, not to mess with pressing keys: a,s
        self.focus()
        
         
         
    def setPreviousXY(self, event):
            print("now")
            self.previousX = event.x
            self.previousY = event.y
             
    def draw(self, event):
        # line 1
        if self.radiobuttonValue.get() == 1:
            self.myCanvas.create_oval(event.x - self.toolsThickness,
                                      event.y - self.toolsThickness,
                                      event.x + self.toolsThickness,
                                      event.y + self.toolsThickness,
                                      fill = self.rgb
                                      )
        #line 2
        elif self.radiobuttonValue.get() == 2:
            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width = self.toolsThickness,
                                      fill = self.rgb)
            self.previousX = event.x
            self.previousY = event.y  
        #flowers tool         
        elif self.radiobuttonValue.get() == 3:
            tk_rgb = "#%02x%02x%02x" % (randint(140,255), randint(140,225), 40)
            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width = self.toolsThickness,
                                      fill = tk_rgb)
        # spray tool
        elif self.radiobuttonValue.get() == 4:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
             
            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + xrand + self.toolsThickness, event.y + yrand + self.toolsThickness,
                                      fill = self.rgb,
                                      width = 0
                                      )  
        # cosmos tool    
        elif self.radiobuttonValue.get() == 5:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            tk_rgb = "#%02x%02x%02x" % (randint(5,255), randint(10,150), randint(13,255))
            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + self.toolsThickness, event.y + self.toolsThickness,
                                      fill = tk_rgb
                                      )
    def delteAll(self):
        self.myCanvas.delete("all")
         
    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)
 
    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)
         
root = Tk()
root.title("Drawing program")
app = Application(root)
root.mainloop() 
