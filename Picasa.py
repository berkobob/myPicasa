"""
30/11/17: My attempt to recreate Picasa. This file is the main and the controller
"""
from view import PicasaView
from data import PicasaData

def controller(command=None, *parms):
    """ all screen clicks are passed here to decide which function to run """
    if command is 'stop':
        print("Bye!")
        view.stop()
    elif command is 'watch':
        data.addfolders(view.getdir())
        view.buildTree(data.folders)
    elif command is 'status':
        view.addstatus(parms)
    else:
        view.addstatus(str(command)+" not yet implemented")

if __name__ == '__main__':
    data = PicasaData(controller)
    view = PicasaView(controller)           # Create the main screen view
    view.start()                            # Start the app
