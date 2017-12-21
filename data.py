"""
09/12/17: The MyPicasa database
"""

from os import walk, path
from json import dump, load
from PIL import Image, ExifTags
from datetime import datetime

class PicasaData():
    """ Interface to the data class """
    def __init__(self, controller):
        self.controller = controller
        self.stamp = datetime.now().isoformat()

        try:
            with open('album.json') as f:
                self.album = load(f)
            # This should be done in a separate thread
            for folder in self.album:
                if folder['top']:                       # There must always be one top is true
                    self.findfolders(folder['path'])    # look for new folders
            self.lostfolders()
        except FileNotFoundError:
            self.album = []                             # brand new empty album


    def findfolders(self, top):
        """ given apath find all folders and pictures and add to album """
        for apath, __, pics in walk(top):
            apath = apath.replace('\\', '/')

            f = next((fol for fol in self.album if fol['path'] == apath), False)
            if f:
                self.controller('status', 'Already watching: ', apath)
                f['stamp'] = self.stamp
                # here we need to find new photos (and ID missing?)
            else:
                f = {'top': top is apath,
                     'folder': apath.split('/')[apath.count('/')],
                     'path': apath,
                     'pics': self.findpics(apath, pics),
                     'stamp': self.stamp}

                self.album.append(f)
                self.controller('status', "Now watching: ", apath)


    def findpics(self, apath, pics):
        """ given list of pics delete check each exists and add new ones """
        Images = []
        for pic in pics:
            p = path.join(apath, pic)
            p = p.replace('\\', '/')
            try:
                img = Image.open(p)
                try:
                    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items()
                            if k in ExifTags.TAGS}
                except AttributeError:
                    #self.controller('status', p, " has no meta data")
                    w, h = img.size
                    exif = {'ExifImageHeight': h,
                            'ExifImageWidth': w}
                image = {'path': p}
                image['orientation'] = exif['Orientation'] if 'Orientation' in exif.keys() else 0
                image['dateTime'] = exif['DateTime'] if 'DateTime' in exif.keys() else 0
                image['height'] = exif['ExifImageHeight'] if 'ExifImageHeight' in exif.keys() else 0
                image['width'] = exif['ExifImageWidth'] if 'ExifImageWidth'in exif.keys() else 0
                #image = {'GPSInfo': exif['GPSInfo']  if 'GPSInfo' in exif else 0}
                Images.append(image)

            except OSError:
                pass #self.controller('status', apath, '/', pic, ' is not a valid pic')

        return Images

    #def buildthumbs

    def lostfolders(self):
        """ examine each folder to check stamp was updated """
        for folder in self.album:
            if folder['stamp'] is not self.stamp:
                self.controller('status', folder['folder'], ' is missing')

        missing = (folder for folder in self.album if folder['stamp'] is not self.stamp)
        for each in missing:
            print(each['path'])
    
    def save(self):
        """ save the album to disk """
        with open('album.json', 'w') as f:
            dump(self.album, f, indent=2)


def cont(*data):
    print(data)

if __name__ == '__main__':
    data = PicasaData(cont)
    #print(data.album)
    #data.findfolders('Pics')
    #print(data.album)
    data.save()

