from imager.imager2 import Imager
import random


def mosaic(fid, numberOfTiles):
    image = Imager(fid)
    x = image.xmax
    y = image.ymax
    tileScale = int(x/numberOfTiles)
    new_x = tileScale*numberOfTiles
    new_y = int(y/tileScale)*tileScale
    scaled = image.resize(new_x, new_y)

    def get_tile(startx, starty):
        tile = []
        for x in range(startx, startx+tileScale):
            for y in range(starty, starty+tileScale):
                tile.append(scaled.get_pixel(x, y))
        return tile

    def build_tile(startxb, startyb):
        tile = tiles[random.randint(0, len(tiles)-1)]
        for x2 in range(startxb, startxb+tileScale):
            for y2 in range(startyb, startyb+tileScale):
                scaled.set_pixel(x2, y2, tile[(x2-startxb)*(y2-startyb)])

    tiles = []

    for x2 in range(0, new_x, tileScale):
        for y2 in range(0, new_y, tileScale):
            tiles.append(get_tile(x2, y2))

    for w in range(0, new_x, tileScale):
        for z in range(0, new_y, tileScale):
            build_tile(w, z)

    scaled.display()

def mosaic2(image, numberOfTiles):
    x = image.xmax
    y = image.ymax
    tileScale = int(x/numberOfTiles)
    new_x = tileScale*numberOfTiles
    new_y = int(y/tileScale)*tileScale
    scaled = image.resize(new_x, new_y)
    print(new_x, new_y, tileScale)

    def get_tile(startx, starty):
        tile = []
        for x in range(startx, startx+tileScale):
            for y in range(starty, starty+tileScale):
                tile.append(scaled.get_pixel(x, y))
        return tile

    def build_tile(startxb, startyb):
        tile = tiles[random.randint(0, len(tiles)-1)]
        for x2 in range(startxb, startxb+tileScale):
            for y2 in range(startyb, startyb+tileScale):
                scaled.set_pixel(x2, y2, tile[(x2-startxb)*tileScale+(y2-startyb)])

    tiles = []

    for x2 in range(0, new_x, tileScale):
        for y2 in range(0, new_y, tileScale):
            print("Gathering", x2, y2)
            tiles.append(get_tile(x2, y2))

    for w in range(0, new_x, tileScale):
        for z in range(0, new_y, tileScale):
            print("Building", w, z)
            build_tile(w,z)


    return scaled

# im1 = mosaic2("images/campus.jpeg", 16)
# im2 = mosaic2("images/campus.jpeg", 16)
# im1.morph(im2).display()