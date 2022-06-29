from tkinter import *
# ##create root window
root=Tk()
# ##root window title and dimension
root.title("surajit_calculator")
root.geometry('350x200')
## using pack geometry widget
# label = Label(root, text ="Hello World !")
# label.pack()
# button=Button(root, text ='Geek')  
# button.pack() 
# using grid geometry widget
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()
root.mainloop()
