
class ChannelChanger(object):

    def xor(self, image, r, g, b):
        for x in range(image.xmax):
            for y in range(image.ymax):
                px = image.get_pixel(x, y)
                red = px[0] ^ r
                green = px[1] ^ g
                blue = px[2] ^ b
                image.set_pixel(x, y, (red, green, blue))

        image.display()
        return image

    def remove_channels(self, image, r, g, b):

        for x in range(image.xmax):
            for y in range(image.ymax):
                red, green, blue = image.get_pixel(x, y)

                red = red if not r else 0
                green = green if not g else 0
                blue = blue if not b else 0

                image.set_pixel(x, y, (red, green, blue))

        image.display()
        return image
