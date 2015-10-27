class Helpers:

    @staticmethod
    def get_red(image):
        xmax = image.size[0]
        y = int(image.size[1]/2)
        #xmax = image.xmax
        #y = int(image.xmax/2)
        sum = 0
        num = 0
        thr = 3
        reds = []
        for x in range(0, xmax, 16):
            pix = image.getpixel((x, y))
            #pix = image.get_pixel(x, y)
            d1 = pix[0]/pix[1] if pix[1] != 0 else 255
            d2 = pix[0]/pix[2] if pix[2] != 0 else 255
            if (d1 > thr) and (d2 > thr):
                sum += x
                num += 1
                reds.append(True)
            else:
                reds.append(False)
        if num != 0:
            pos = ((sum/num) - (xmax/2))/(xmax/2)
        else:
            pos = 0
        print(reds, pos)
        return (num*16/xmax)*1000, pos
