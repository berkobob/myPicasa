import tkinter as tk

root = tk.Tk()

LAR = tk.PanedWindow(root, orient=tk.HORIZONTAL)
LAR.grid(sticky='nsew')

leftpane = tk.Label(LAR, text='Left Pane')
LAR.add(leftpane, stretch="always")

rightpane = tk.Button(LAR, text="Right Pane")
LAR.add(rightpane, stretch="always")

bottompane = tk.Label(root, text="Bottom pane label")
bottompane.grid(row=1, sticky='ew')

LAR.config(sashwidth=2, showhandle=True, handlepad=10, sashrelief='raised')

root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(1, weight=2)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

root.mainloop()
