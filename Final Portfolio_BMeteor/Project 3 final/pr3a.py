from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from gradientmask import gradientmask

#open the original image
im = Image.open("final.jpg")
px = im.load()



Sharpness = ImageEnhance.Sharpness(im)
im2 = im.filter(ImageFilter.SHARPEN)


for x in range(0,im.width):
    for y in range(0,im.height):
        # Retriev the Red, Green and Blue value of the pixel
        R = px[ x, y ][0]
        G = px[ x, y ][1]
        B = px[ x, y ][2]

        invertedR = R + 85
        invertedG = G - 70
        invertedB = 75 + B




        

   


		# Do something amazing here to change R G and B!





		# Now we use our new R G B values to update the pixel.
        px[x,y] = ( invertedR, invertedG, invertedB )

im.show()
im.save("Finaldesign.png")
