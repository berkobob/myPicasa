"""
30/11/17: The menu bar for Picasa
"""
from tkinter import Menu

class PicasaMenu(Menu):
    """ Main menu bar """
    def __init__(self, parent, controller):
        self.controller = controller                        # Call to do stuff
        Menu.__init__(self, parent)                         # Call Menu parent init

        self.file_menu = Menu(self)                         # create file menu
        self.file_menu.add_command(label="Watch",           # add Watch to file menu
             command=self.controller)
        self.file_menu.add_separator()                      # have quit on it's own
        self.file_menu.add_command(label='Quit',            # add quit to file memu
             command=lambda: self.controller('stop'))
        self.add_cascade(label="File", menu=self.file_menu) # add file menu to menu

def controller():
    """ A controller just for testing """
    print("Controlling from menu.py")

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    menu = PicasaMenu(root, controller)
    root.config(menu=menu)
    root.mainloop()
