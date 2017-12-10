"""
09/12/17: The MyPicasa database
"""

from os import walk

class PicasaData():
    """ Interface to the data class """
    def __init__(self, controller=None):
        self.controller = controller
        self.folders = []

    def addfolders(self, path):
        """ given a path find all folders and pictures and add to album """
        for dir, b, c in walk(path):
            dir = dir.replace('\\', '/')

            if [x for x in self.folders if x['path'] == dir]:
                #print("Already watching", dir)
                self.controller('status', 'Already watching: ', dir)
            else:
                f = dir.split('/')[dir.count('/')]

                folder = {'folder': f,
                          'path': dir}

                self.folders.append(folder)

if __name__ == '__main__':
    data = PicasaData()
    data.addfolders('.')
