import imager2
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps
from random import randint

class TrippyImages():

    def __init__(self, imager2):
        self.imager = imager2

    def display(self):
        self.imager.display()

    def set_image(self, image):
        self.imager.set_image(image)

    def trippy_rotated(self,newsize=500):
        im1 = self.imager; im2 = self.imager
        im1 = im1.resize(newsize,newsize); im2 = im2.resize(newsize,newsize)
        im2.set_image(im2.get_image().rotate(180))
        combined = Imager.map_color_wta(im1.morph(im2), thresh=0.25)
        combined = combined.get_image().filter(ImageFilter.EDGE_ENHANCE_MORE)
        return combined

    def black_white(self, newsize=500):
        im1 = self.imager
        im1 = im1.resize(newsize, newsize)
        im1.set_image(ImageEnhance.Color(im1.get_image().filter(ImageFilter.SHARPEN)).enhance(0))
        return im1.get_image()

    def invert_colors(self):
        return ImageOps.invert(self.imager.image).filter(ImageFilter.SMOOTH_MORE)

    def emboss(self):
        return self.imager.get_image().filter(ImageFilter.EMBOSS)

    def randomly_invert_pixels(self):
        self.imager.get_image_dims()
        for i in range(self.imager.xmax):
            for j in range(self.imager.ymax):
                pixel = self.imager.get_pixel(i, j)
                newPixel = []
                for x in range(3):
                    newPixel.append(randint(255, 255 + pixel[x]) - pixel[x])
                pixel = (newPixel[0], newPixel[1], newPixel[2])
                self.imager.set_pixel(i, j, pixel)

im = imager2.Imager("images/einstein.jpeg")
trippy = TrippyImages(im)
trippy.set_image(trippy.emboss())
trippy.display()

'''
im = Imager("images/einstein.jpeg")
im.display()
im.set_image(im.trippy_rotated())
im.display()
im.set_image(im.invert_colors())
im.display()
im = Imager("images/einstein.jpeg").resize(500,500)
im.display()
im = im.tunnel()
im.set_image(im.invert_colors())
im.set_image(im.black_white())
im.set_image(im.trippy_rotated())
im.display()
im2 = Imager("images/einstein.jpeg").resize(500,500)
im2.set_image(im2.invert_colors())
im = im.morph(im2, alpha=0.5)
#im.display()
im.display()
'''
'''

im = Imager("images/einstein.jpeg")
im.display()
im.randomly_invert_pixels()
im.display()
'''