"""
30/11/17: My attempt to recreate Picasa. This file is the main and the controller
"""
from view import PicasaView
from data import PicasaData

def controller(command=None, *parms):
    """ all screen clicks are passed here to decide which function to run """
    if command is 'stop':
        print("Bye!")
        data.save()
        view.stop()
    elif command is 'watch':
        data.addfolders(view.getdir())
        view.build(data.folders)
    elif command is 'status':
        view.addstatus(parms)
    elif command is 'clear':
        view.clearstatus()
    else:
        view.addstatus(str(command)+" not yet implemented")

if __name__ == '__main__':
    view = PicasaView(controller)           # Create the main screen view
    data = PicasaData(controller)
    view.build(data.folders)
    view.start()                            # Start the app
