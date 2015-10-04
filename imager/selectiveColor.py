from imager.imager2 import Imager


def selective_color(fid, color, tolerance):
    image = Imager(fid)

    def equal(pix1, pix2):
        l1 = pix1[0]/pix1[1] if pix1[1] != 0 else 0
        l2 = pix1[0]/pix1[2] if pix1[2] != 0 else 0
        s1 = pix2[0]/pix2[1] if pix2[1] != 0 else 0
        s2 = pix2[0]/pix2[2] if pix2[2] != 0 else 0

        equal1 = l1 < s1 + tolerance and l1 > s1 - tolerance
        equal2 = l2 < s2 + tolerance and l2 > s2 - tolerance
        return not (equal1 and equal2)



    def bw(pixel):
        lum = int((pixel[1] + pixel[2] + pixel[0])/3)
        return lum, lum, lum

    for y in range(image.ymax):
        for x in range(image.xmax):
            pixel = image.get_pixel(x, y)
            if equal(pixel, color):
                image.set_pixel(x, y,  bw(pixel))

    image.display()


selective_color("images/campus.jpeg", (105, 75, 65), 0.4)

