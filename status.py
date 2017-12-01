"""
30/11/17: Add all the status comment to a scrolling text field
"""

from tkinter import Text, Scrollbar, Frame

class Status(Frame):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, controller=None):
        Frame.__init__(self, parent)
        self.controller = controller
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.text = Text(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        self.text.grid(row=0, column=0, stick='nsew')
        self.grid(row=0, column=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.text.insert((1.0), "Status bar")


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    Status(root).grid()
    root.mainloop()
