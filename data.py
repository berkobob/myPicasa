"""
09/12/17: The MyPicasa database
"""

from os import walk, path
from json import dump, load

class PicasaData():
    """ Interface to the data class """
    def __init__(self, controller):
        self.controller = controller
        """
        try:
            with open('settings.json') as f:
                self.settings = load(f)
        except FileNotFoundError:
            self.settings = dict()
        """
        try:
            with open('album.json') as f:
                self.folders = load(f)
            # This should be done in a separate thread
            for folder in self.folders:
                if folder['top']:
                    # rename apath to path and find a way of using path.join
                    self.addfolders(folder['apath'])
        except FileNotFoundError:
            self.folders = []


    def addfolders(self, top):
        """ given a apath find all folders and pictures and add to album """
        for apath, __, pics in walk(top):
            apath = apath.replace('\\', '/')

            if [x for x in self.folders if x['apath'] == apath]:
                self.controller('status', 'Already watching: ', apath)
            else:
                folder = apath.split('/')[apath.count('/')]

                f = {'top': top is apath,
                     'folder': folder,
                     'apath': apath}

                self.folders.append(f)
                self.controller('status', "Now watching: ", apath)

                for pic in pics:
                    f = os.path.join(apath, pic)
                    print(f)

    def save(self):
        """ save the album to disk """
        with open('album.json', 'w') as f:
            dump(self.folders, f)


def cont(*data):
    print(data)

if __name__ == '__main__':
    data = PicasaData(cont)
    print(data.folders)
    data.addfolders('Pics')
    print(data.folders)
    data.save()
