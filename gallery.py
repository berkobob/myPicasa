"""
30/11/17: Display all the photos in one big long streaming canvas
"""

from tkinter import Canvas, Label

class Gallery(Canvas):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, cont):
        self.controller = cont
        Canvas.__init__(self, parent)

    def build(self, album):
        """ display thumbnail photos """
        for folder in album:
            Label(self, text=folder['folder']).grid()


def controller(text, *args):
    """ controller for testing purposes """
    txt = ""
    for msg in args:
        txt += msg
    print(text, txt)

if __name__ == '__main__':
    from tkinter import Tk
    from data import PicasaData

    root = Tk()
    data = PicasaData(controller)
    view = Gallery(root, controller)
    view.build(data.album)
    view.grid()

    root.mainloop()
    