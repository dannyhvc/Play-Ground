from tkinter import *
from tkinter import ttk
import tkinter as tk


def mygui1():
    #boilerplate code
    root = Tk()
    root.title("Welcome to the Gui1")
    #initializing components
    e1 = Entry(root)
    b1 = Button(root, command=lambda: print(e1.get()))

    b1.grid(column=0, row=1)
    e1.grid(column=1, row=1)

    #shows/ start the gui
    root.mainloop()


def lyndagui1():
    root = Tk()
    button = ttk.Button(root, text='click me')
    button.pack()

    # changes the buttons text from click me, to press me.
    button['text'] = 'press me'
    # same as line above, but uses different format.
    button.config(text='push me')
    # if no params are passed the this prints all available params for the
    print(button.config())
    # widget.

    # shows the gui
    root.mainloop()


class LG1:
    """
    This is a small adaptation of what the current guis will be like
    """

    def __init__(self, master):
        self.__presses = 0
        button = ttk.Button(master, text='Press!', command=self.eventLG1)
        button.pack()

    def eventLG1(self):
        self.__presses += 1
        print(f"pressed: {self.__presses}")


class LG2:

    def __init__(self, master):
        # instance variables
        self.__uname = ''
        self.__passw = ''

        # <<BOILERPLATE CODE>>
        ttk.Label(master, text='Username:').grid(row=0, column=0)
        self.uname_ebox = ttk.Entry(master)
        self.uname_ebox.grid(row=1, column=0)

        ttk.Label(master, text='Password:').grid(row=2, column=0)
        self.passw_ebox = ttk.Entry(master, show='*')
        self.passw_ebox.grid(row=3, column=0)

        self.button = ttk.Button(master, text='Enter', command=self.getData)
        self.button.grid(row=2, column=1, columnspan=4)

    def getData(self):
        if self.uname_ebox.get() != '' and self.passw_ebox.get() != '':
            self.__uname = self.uname_ebox.get()
            self.__passw = self.passw_ebox.get()
            print(f'Username: {self.__uname}\nPassword: {self.__passw}\n')

        else:
            print("N/A")

        self.uname_ebox.delete(0, 'end')
        self.passw_ebox.delete(0, 'end')


#########################################################################################################################

# python kivy applications
import kiwisolver as kiwi

kiwi.Variable('x')