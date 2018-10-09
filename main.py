from Tkinter import *
import Tkconstants, tkFileDialog

master = Tk()

def loadFile():
    filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PDF Files","*.pdf"),("all files","*.*")))
    l1['text'] = filename
    print filename

def ShowChoice():
    print v.get()






master.title("PDF ToolKit 1.0")

v = IntVar()
v.set(1)

l = Label(master, text="INFO: A Python FrameWork for PDFs")
l.grid(row =0,padx =5, pady =5, columnspan = 2)

b1 = Button(master, text='Load a PDF', command=loadFile)
b1.grid(row=1, column=0, sticky=W,padx =5, pady =5)
b1.config(width = 20 )
b2 = Button(master, text='Extract Text', command=loadFile)
b2.grid(row=1, column=0, sticky=W,padx =5, pady =5)
b2.config(width = 20 )

l1 = Label(master, text="")
l1.grid(row=1,column=1, padx =5, pady =5)
l1.config(width = 20 )
l2 = Label(master, text="")
l2.grid(row=3, padx =5, pady =5)
l2.config(width = 20 )



e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=2, column=1, padx =5, pady =5)
e2.grid(row=3, column=1, padx =5, pady =5)

master.mainloop()
# mainloop( )

#print eval(e1.get()) * eval(e2.get())