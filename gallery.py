"""
30/11/17: Display all the photos in one big long streaming canvas
"""

from tkinter import Button, Frame

class Gallery(Frame):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, cont):
        self.controller = cont
        Frame.__init__(self, parent)
        Button(self, text="Gallery on right", command=cont).grid()

    def build(self, folders):
        """ display thumbnail photos """
        for folder in folders:
            print("Building gallery", folder)


def controller(text=None):
    """ controller for testing purposes """
    print("In albums: ", text)

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    Gallery(root, controller).grid()
    root.mainloop()