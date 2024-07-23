import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=400)

# Label

my_Label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_Label.pack()












window.mainloop()