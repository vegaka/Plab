from imager.imager2 import Imager
from imager.channelChanger import ChannelChanger
from imager.trippy_images import TrippyImages

class ArtMaker(object):

    def __init__(self, files):
        self.images = self.loadImages(files)
        self.channelChanger = ChannelChanger()
        self.trippy_images = TrippyImages()

    def loadImages(self, files):
        return [Imager(path) for path in files]
