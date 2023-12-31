from tkinter import *
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.pack()  # how to create widgets
b2.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10) 

Win = Tk()
b1 = Button(Win, text="One")
b2 = Button(Win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
l = Label(Win, text="This is a label")
l.grid(row=1, column=0)

Win = Tk()
f = Frame(Win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(Win, text="This label is over all buttons")
l.pack()
f.pack()
b1.configure(text="Uno")

#input text from the user
win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
v.get()
'This is a test'
v.set("this is set by the program")

# widget give menu of items to choose from
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection() # return the selected item for you. It returns a tuple of items selected.