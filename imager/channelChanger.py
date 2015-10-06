
class ChannelChanger(object):

    def __init__(self, image):
        self.image = image

    def xor(self, r, g, b):
        for x in range(self.image.xmax):
            for y in range(self.image.ymax):
                px = self.image.get_pixel(x, y)
                red = px[0] ^ r
                green = px[1] ^ g
                blue = px[2] ^ b
                self.image.set_pixel(x, y, (red, green, blue))

        self.image.display()

    def remove_channels(self, r, g, b):

        for x in range(self.image.xmax):
            for y in range(self.image.ymax):
                red, green, blue = self.image.get_pixel(x, y)

                red = red if not r else 0
                green = green if not g else 0
                blue = blue if not b else 0

                self.image.set_pixel(x, y, (red, green, blue))

        self.image.display()
