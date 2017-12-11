"""
09/12/17: The MyPicasa database
"""

from os import walk
from json import dump, load

class PicasaData():
    """ Interface to the data class """
    def __init__(self, controller=None):
        self.controller = controller
        self.folders = []
        try:
            with open('album.json') as f:
                self.folders = load(f)
        except:
            pass


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

    def save(self):
        """ save the album to disk """
        with open('album.json', 'w') as f:
            dump(self.folders, f)

if __name__ == '__main__':
    data = PicasaData()
    print(data.folders)
    data.addfolders('.')
    print(data.folders)
    data.save()
