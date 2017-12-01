import tkinter as tk

x = 1

def test():
    global x
    bottomframe.insert((1.0), "line number " + str(x) +"\n")
    x += 1

root = tk.Tk()

TAB = tk.PanedWindow(root, orient=tk.VERTICAL)
TAB.grid(sticky='nsew')

LAR = tk.PanedWindow(root, orient=tk.HORIZONTAL)
LAR.grid(sticky='nsew')

TAB.add(LAR)

leftpane = tk.Label(LAR, text='Left Pane')
LAR.add(leftpane)

rightpane = tk.Button(LAR, text="Right Pane", command=test)
LAR.add(rightpane, stretch="always")

frame = tk.Frame(TAB)
frame.grid(sticky='nsew')
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

scrollbar = tk.Scrollbar(frame)#
scrollbar.grid(row=0, column=1, sticky='ns')#

bottomframe = tk.Text(frame, yscrollcommand=scrollbar.set)#
scrollbar.config(command=bottomframe.yview)

bottomframe.grid(row=0, column=0, sticky='nsew')
TAB.add(frame)

bottomframe.insert((1.0), "Bottom pane label1\n")
bottomframe.insert((1.0), "Bottom pane label2\n")
bottomframe.insert((1.0), "Bottom pane label3\n")

TAB.config(sashwidth=2, showhandle=True, handlepad=10, sashrelief='raised')
LAR.config(sashwidth=2, showhandle=True, handlepad=10, sashrelief='raised')

root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)
#root.grid_rowconfigure(1, weight=1)

root.mainloop()
