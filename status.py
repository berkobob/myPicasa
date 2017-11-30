"""
30/11/17: Add all the status comment to a scrolling text field
"""

from tkinter import Button, Frame

class Status(Frame):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        Button(self, text="Status at the bottom", command=controller).grid()


def controller(text=None):
    """ controller for testing purposes """
    print("In albums: ", text)

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    Status(root, controller).grid()
    root.mainloop()