from tkinter import *
root = Tk()
root.geometry("1360x687")

c = Canvas(root, bg="white", height=600, width=1000)

#Code for swastika
#id = c.create_oval(100,100, 400,300, width=3, fill='white', outline='red', activefill='red') 
#id = c.create_line(200,100, 200,200, 350,200, 350,300, width=5, fill="black")
#id = c.create_line(350,100, 275,100, 275,300, 200,300, width=5, fill="black")


id = c.create_arc(100,300, 200,400, width=3, start=180, extent=180, outline="black", style="arc")
id = c.create_arc(200,300, 300,400, width=3, start=180, extent=180, outline="black", style="arc")
c.pack()

root.mainloop()

