"""
09/12/17: The MyPicasa database
"""

from os import walk, path
from json import dump, load
from PIL import Image, ExifTags

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
                    self.addfolders(folder['path'])
        except FileNotFoundError:
            self.folders = []


    def addfolders(self, top):
        """ given a apath find all folders and pictures and add to album """
        for apath, __, pics in walk(top):
            apath = apath.replace('\\', '/')

            if [x for x in self.folders if x['path'] == apath]:
                self.controller('status', 'Already watching: ', apath)
            else:
                folder = apath.split('/')[apath.count('/')]
                album = self.addpics(apath, pics)

                f = {'top': top is apath,
                     'folder': folder,
                     'path': apath,
                     'pics': album}

                self.folders.append(f)
                self.controller('status', "Now watching: ", apath)

                


    def addpics(self, apath, pics):
        """ given list of pics delete check each exists and add new ones """
        Images = []
        for pic in pics:
            p = path.join(apath, pic)
            p = p.replace('\\', '/')
            try:
                img = Image.open(p)
                try:
                    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
                except AttributeError:
                    self.controller('status', p, "has no meta data")
                    w, h = img.size
                    exif = {'ExifImageHeight': h,
                            'ExifImageWidth': w}
                if 'Orientation' in exif.keys():
                    Orientation = exif['Orientation']
                else:
                    Orientation = 0
                if 'DateTime' in exif.keys():
                    DateTime = exif['DateTime']
                else:
                    DateTime = 0
                if 'ExifImageHeight' in exif.keys():
                    Height = exif['ExifImageHeight']
                else:
                    Height = 0
                if 'ExifImageWidth'in exif.keys():
                    Width = exif['ExifImageWidth']
                else:
                    Width = 0
                if 'GPSInfo' in exif:
                    GPSInfo = exif['GPSInfo']
                else:
                    GPSInfo = 0

                image = {'Path': p,
                         'Orientation': Orientation,
                         'DateTime': DateTime,
                         'Height': Height,
                         'Width': Width,
                         'GPSInfo': str(GPSInfo)}
                Images.append(image)
                print(image)
            except OSError:
                self.controller('status', apath, pic, 'is not a valid pic')
 

        return Images

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
