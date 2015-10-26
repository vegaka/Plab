
class Helpers:

    @staticmethod
    def get_red(image):
        rth = 70
        pth = 35
        rows = []
        sums = []
        total = 0
        num = 0
        numOfPixels = 0
        xmax = image.size[0]
        ymax = image.size[1]
        for y in range(ymax):
            reds = []
            sum = 0
            div = 0
            for x in range(xmax):
                pix = image.getpixel((x, y))
                is_red = (pix[0] > rth)
                not_red = (pix[1]+pix[2])/2 < pth
                reds.append(is_red and not_red)
                sum += x*int(is_red)
                div += int(is_red)
                numOfPixels += int(is_red)
            rows.append(reds)
            ans = sum/div if div != 0 else 0
            sums.append(int(ans))
            total += int(ans)
            if int(ans) != 0:
                num += 1
            ret = ((total / num if num != 0 else 0)-xmax/2)/(xmax/2)
        return ret, numOfPixels/(xmax*ymax)*100
