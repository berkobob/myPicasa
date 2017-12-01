"""
30/11/17: My attempt to recreate Picasa. This file is the main and the controller
"""
from view import PicasaView

def controller(command=None):
    """ all screen clicks are passed here to decide which function to run """
    if command is 'stop':
        print("Bye!")
        view.stop()
    elif command is 'quit':
        pass
    else:
        view.addstatus(str(command)+" not yet implemented")

if __name__ == '__main__':
    view = PicasaView(controller)           # Create the main screen view
    view.start()                            # Start the app
