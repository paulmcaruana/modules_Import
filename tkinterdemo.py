try:
    import tkinter
except ImportError:   # python 2
    import Tkinter as tkinter


print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()        leave this in to see the window with the version, quit etc

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x640+8+400')
mainWindow.mainloop()

