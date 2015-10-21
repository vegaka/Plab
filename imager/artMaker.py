from imager.imager2 import Imager
from imager.channelChanger import ChannelChanger
from imager.trippy_images import TrippyImages
from imager.enhance import *
from imager.selectiveColor import *
from imager.mosaic import *

class ArtMaker(object):

    def __init__(self, files):
        self.images = self.loadImages(files)
        self.channelChanger = ChannelChanger()
        self.trippy_images = TrippyImages()

    def loadImages(self, files):
        return [Imager(path) for path in files]



fib = Imager("images/fibonacci.jpeg")
stairs = Imager("images/stairs.jpeg")
donald = Imager("images/donaldduck.jpeg")

fibstair = combine(fib, stairs)
# fibstair = selective_color(fibstair, (251, 226, 22), 0.8)
fibstair.display()

donald = mosaic2(donald, 4)
donald = TrippyImages(donald)
donald.randomly_invert_pixels()
donald = donald.get_imager()
donald.display()
