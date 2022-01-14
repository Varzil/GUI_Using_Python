import tkinter

# Importing the tkinter

window = tkinter.Tk()
# This line makes a window We need to call the main loop to make window visible

window.title("Hello Tkinter")
# Makes title

window.minsize(width=300, height=500)
# sets h,w

mylabel = tkinter.Label(text="Hello Varzil", background="black")
# creates label but does not show on screen use .pack method to show on screen

mylabel.pack()

window.mainloop()
# This line should be at the end
