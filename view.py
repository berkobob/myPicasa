"""
20/11/17: The view file in the MVC Model for My Picasa
"""

from tkinter import Tk, PanedWindow, VERTICAL, HORIZONTAL, filedialog
from menu import PicasaMenu
from tree import Tree
from gallery import Gallery
from status import Status

class PicasaView():
    """ Interface to the view class """
    def __init__(self, controller):
        self.controller = controller                        # function to call

        self.root = Tk()                                    # create main window called root
        self.root.state('zoomed')                           # have root be full screen
        self.root.title('Picasa')                           # name the display
        self.root.protocol('WM_DELETE_WINDOW',
             lambda: self.controller('stop'))               # Trap close window

        self.menu = PicasaMenu(self.root, controller)       # create main menu
        self.root.config(menu=self.menu)                    # add menu to window

        self.TAB = PanedWindow(self.root, orient=VERTICAL)  # Top And Bottom
        self.TAB.grid(sticky='nsew')
        self.LAR = PanedWindow(self.root, orient=HORIZONTAL)# Left And Right
        self.LAR.grid(sticky='nsew')
        self.TAB.add(self.LAR)        

        self.tree = Tree(self.root, controller)             # create tree                           
        self.LAR.add(self.tree)

        self.gallery = Gallery(self.root, controller)       # create all pics
        self.LAR.add(self.gallery)

        self.status = Status(self.TAB, controller)         # create status text
        self.TAB.add(self.status)

        self.TAB.config(sashrelief='raised')                # make sash visible
        self.LAR.config(sashrelief='raised')

        self.root.grid_columnconfigure(0, weight=1)         # make all resizeable
        self.root.grid_rowconfigure(0, weight=1)

        self.TAB.sash_place(0, 1, 1000)
        #self.TAB.sash('dragto', 0, 1, 1000)

    def start(self):
        """ start the main window """
        self.root.mainloop()                                # display root

    def stop(self):
        """ quit Picasa and close down cleanly """
        self.root.destroy()                                 # Quit the application
        #self.root.quit()

    def addstatus(self, text):
        """ add a comment to the status log """
        txt = ""
        for msg in text:
            txt += msg
        self.status.text.insert((1.0), txt+'\n')

    def clearstatus(self):
        """ clear the contents of the status area """
        self.status.text.delete((1.0), 'end')

    def getdir(self):
        """ Get the user to choose a folder to watch """
        return filedialog.askdirectory()

    def build(self, folders):
        """ build tree structure and gallery from list of folders """
        self.tree.build(folders)
        self.gallery.build(folders)

def cont(dump=None):
    """ a controller just for testing """
    if dump is 'stop':
        screen.stop()
    elif dump is 'watch':
        for a, b, c in screen.getdir():
            print(a)
            print(b)
    else:
        print("Controlling from view.py", dump)
        print(screen.TAB.sash_coord(0))

if __name__ == '__main__':
    screen = PicasaView(cont)
    screen.start()
