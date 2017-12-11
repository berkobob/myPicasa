"""
30/11/17: Display all the albums we're watching for photos
"""
from tkinter import Button, Frame, ttk

class OldTree(Frame):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)
        Button(self, text="Tree on left", command=controller).grid()

class Tree(ttk.Treeview):
    """ Display a list of folders and scroll to each one when clicked """
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Treeview.__init__(self, parent)
        self.heading('#0', text="Albums", anchor='w')
        self.bind('<<TreeviewSelect>>', self.onClick)

    def onClick(self, event):
        """ ? """
        ab=self.item(self.selection()[0])['text']
        print(ab)
        print("self.focus", self.item(self.focus()))
        print("self.selection()[0]", self.selection()[0])
        print("Event", event)
        self.controller(ab) 
    
    def build(self, folders):
        """ create tree structure from list of folders """
        #x=self.get_children() for item in x: self.delete(item)
        for i in self.get_children():
            self.delete(i)
            
        for folder in folders:
            self.insert('', 'end', text=folder['folder'])


def cont(text=None):
    """ controller for testing purposes """
    print("In albums: ", text)

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    t = Tree(root, cont)
    t.grid(sticky='nsew')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    for i in range(20):
        a = t.insert('', 'end', text=str(i))
        if i % 3 == 0:
            for j in range(4):
                t.insert(a, 'end', text=str(j))

    root.mainloop()
