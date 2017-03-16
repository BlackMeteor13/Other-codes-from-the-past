from PIL import Image, ImageDraw, ImageFilter
import math

def gradientmask(orig,start,end):
    size = (orig.width,orig.height)
    mask = Image.new('L', size, 0)
    maskpx = mask.load()
    blurstart = start
    blurend = end
    for x in range(mask.width):
        for y in range(mask.height):
            distance = math.sqrt(math.pow(x-mask.width/2,2) + math.pow(y-mask.height/2,2))
            normalized = distance / (mask.width/2)
            if normalized > blurstart:
                blurrange = blurend - blurstart
                col = 255 - ((normalized - blurstart) * (1/blurrange)) * 255
                if col < 0:
                    col = 0
            else:
                col = 255
            maskpx[x,y] = math.floor(col)
    return mask
