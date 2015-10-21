from PIL import ImageEnhance
from PIL import ImageFilter
from imager.imager2 import Imager

def edge_enhance(image):
    im1 = ImageEnhance.Color(image.get_image().filter(ImageFilter.EDGE_ENHANCE)).enhance(-100 / 255)
    im1 = ImageEnhance.Sharpness(im1).enhance(2.0)
    im1.show()

def combine(image1, image2):
    w = min(image1.xmax, image2.xmax)
    h = min(image1.ymax, image2.ymax)
    im1 = Imager(width=w, height=h)

    for x in range(w):
        for y in range(h):
            rgb = image1.combine_pixels(image1.get_pixel(x, y), image2.get_pixel(x, y))
            im1.set_pixel(x, y, rgb)

    return im1

# something(Imager("images/einstein.jpeg"))
combine(Imager("images/einstein.jpeg"), Imager("images/fibonacci.jpeg"))
