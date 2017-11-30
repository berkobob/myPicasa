"""
30/11/17: Display all the photos in one big long streaming canvas
"""

from tkinter import Button, Frame

class Gallery(Frame):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        Button(self, text="Gallery on right", command=controller).grid()


def controller(text=None):
    """ controller for testing purposes """
    print("In albums: ", text)

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    Gallery(root, controller).grid()
    root.mainloop()