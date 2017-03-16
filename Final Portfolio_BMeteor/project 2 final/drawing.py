# First, install Pillow in your Terminal:   pip install pillow

# Import two modules from Pillow: Image and ImageDraw

from PIL import Image
from PIL import ImageDraw

# Create a new image with 1000px width, 500px height, and a white background
im = Image.new( "RGB", (1000,500), (255,255,255) )
# Activate the ability to draw on our image.
draw = ImageDraw.Draw( im, 'RGBA' )

# DRAW HERE!
import csv
from pprint import pprint
file = open("vgsales.csv")
data = csv.DictReader( file )
data = list(data)

for i, datafile in enumerate(data):
	sales = float(datafile['NA_Sales'])
	x = sales*41
	y = i*60
	w = 30
	h = 30
	draw.line( (x,y,x+w,y+h), fill=(252,29,36,100) )

for i, datafile in enumerate(data):
	sales = float(datafile['JP_Sales'])
	x = i*4
	y =sales*90
	w = 60
	h = 60
	draw.line((x,y,x+w,y+h), fill=(117,163,143,100) )

for i, datafile in enumerate(data):
	sales = float(datafile['EU_Sales'])
	x = i*29
	y =sales*120
	w = 90
	h = 90
	draw.line((x,y,x+w,y+h), fill=(122,29,252,100))

for i, datafile in enumerate(data):
	sales = float(datafile['Other_Sales'])
	x = i*8.5
	y =sales*150
	w = 120
	h = 120
	draw.line((x,y,x+w,y+h), fill=(252, 166, 29, 100))

for i, datafile in enumerate(data):
	sales = float(datafile['Global_Sales'])
	x = i*83
	y =sales*180
	w = 150
	h = 150
	draw.line((x,y,x+w,y+h), fill=(95, 88, 1, 50))





# Draw a circle. First parameter is x/y coordinates, second parameter is color (see video lesson).



# Preview the image
im.show()
# Save the image
im.save("mydatavis.png")
