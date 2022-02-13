# search_in_depth3a
""" version3 does auto advance at 500 pixels
version 2  working on making w adjust with each zoom
  works with zoom4.  goal: clean and separate auto advance
  into Zoom module
"""

from locale import DAY_3
import sys
from tkinter.messagebox import YESNO
sys.path.append (r'/Users/jillwellman_sept09_2012/Desktop/Python/myProjects/myModules')

import matplotlib.cm
from PIL import Image
import PIL
from graphics import *
from mygraphics import *

from mandelbrot import MandelbrotSet
from viewport import Viewport
from zoom4 import Zoom

X = Y = 500
def paint(mandelbrot_set, viewport, palette, smooth):
	for pixel in viewport:
		stability = mandelbrot_set.stability(complex(pixel), smooth)
		index = int(min(stability * len(palette), len(palette) - 1))
		pixel.color = palette[index % len(palette)]


def denormalize(palette):
	return [
		tuple(int(channel * 255) for channel in color) for color in palette
	]

def DRAW(cx,cy,w):
	print(3*" ...")
	colormap = matplotlib.cm.get_cmap("twilight").colors
	palette = denormalize(colormap)
	mandelbrot_set = MandelbrotSet(max_iterations=512, escape_radius=1000) # 1000
	image = Image.new(mode="RGB", size=(X, Y))
	viewport = Viewport(image, center=cx + cy*1j, width=w)
	paint(mandelbrot_set, viewport, palette, smooth=True)
	print(image)
	return image

winA = GraphWin('winA',500,500)
winA.getMouse()

imW = gImage(Point(X/2,Y/2),'zoom8.png')
imW.draw(winA,'')	
winA.getMouse()

if __name__ == "__main__":



	x,y,w = -0.7435, 0.1314,0.002  #original purple spiral
	dx,dy,fw = 0.0001,0.0001,1.2  # reduction factor for width w
	zm = Zoom(X,Y,x,y,w,fw)

	n = 0
	file_name = 'zoom'+str(n)+'.png'
	# zm.winA = GraphWin('winA',X,Y)
	try: image = PIL.Image.open(file_name)
	except:
		FileNotFoundError
		print('file not found')
		image = DRAW(x,y,w)
		image.save(file_name)
	# print(image)
	# zm.image = image
	zm.file_name = 'zoom'+str(n)+'.png'
	image.save(file_name)
	imW = gImage(Point(X,Y),file_name)
	imW.draw(winA,'')	

	while True:
		n+=1

		x,y,w,dx,dy = zm.auto_deepen(x,y,w,dx,dy)
		print( f"n,x,y,w:  {n:{2}} {x:{1}.{4}}, {y:{1}.{4}}, {w:{1}.{4}}")
		# image = DRAW(x,y,w)
		file_name = 'zoom'+str(n)+'.png'
		try: 
			image = PIL.Image.open(file_name)
			imW = gImage(Point(X/2,Y/2),file_name)
			imW.draw(winA,'')	
		except:
			FileNotFoundError
			break
		

	
		winA.getMouse()
		# zm.image.show()
	




	