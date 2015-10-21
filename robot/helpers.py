from Plab.imager.imager2 import Imager
import statistics as s
class Helpers:

    @staticmethod
    def get_red(image):
        rth = 30
        pth = 10
        rows = []
        sums = []
        total = 0
        num = 0
        numOfPixels = 0
        for y in range(image.ymax):
            reds = []
            sum = 0
            div = 0
            for x in range(image.xmax):
                pix = image.get_pixel(x, y)
                is_red = pix[0] > rth and pix[1] < pth and pix[2] < pth
                reds.append(is_red)
                sum += x*int(is_red)
                div += int(is_red)
                numOfPixels += int(is_red)
            rows.append(reds)
            ans = sum/div if div != 0 else 0
            sums.append(int(ans))
            total += int(ans)
            if int(ans) != 0:
                num += 1
            ret = ((total / num if num != 0 else 0)-image.xmax/2)/(image.xmax/2)
        return ret, numOfPixels/(image.xmax*image.ymax)*100

h = Helpers()
im = Imager("Red.jpg")
print(h.get_red(im))