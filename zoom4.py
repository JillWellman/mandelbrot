# zoom3  020922
"""zoom2.py starts a search in depth
Starting over with purple spiral.  can use much of the zoom
stuff in this file, but will use the tutorial method to zoom
and pan separately.  Bring in window and later click interface."""

import PIL
from PIL import Image
import matplotlib
from pyparsing import java_style_comment
from viewport import Viewport
import viewport
from mandelbrot import MandelbrotSet

import sys
sys.path.append (r'/Users/jillwellman_sept09_2012/Desktop/Python/myProjects/myModules')

from graphics import *
from mygraphics import *
from mandelbrot import MandelbrotSet
from viewport import Viewport
import static_methods

from graphics import *


class Zoom:

	def __init__(self,X,Y,x,y,w,fw) -> None:
		self.X,self.Y = X,Y
		self.x,self.y,self.w = x,y,w
		self.fw = fw
		self.file_name = None
		# self.winA = GraphWin('mandelbrot',X,Y)

	def auto_deepen(self,x,y,w,dx,dy):
		"""coded progress in move and deepen"""
		fw = self.fw
		dx,dy,w = dx/fw,dy/fw, w/fw 
		x,y = x+dx,y+dy 
		return x,y,w,dx,dy

	# def save_and_show(self,n,image):
	# 	# print(image)
	# 	# image.show()
	# 	self.image = image
	# 	self.file_name = 'zoom'+str(n)+'.png'
	# 	self.image.save(self.file_name)
	# 	imW = gImage(Point(self.X/2,self.Y/2),self.file_name)
	# 	imW.draw(self.winA,'')	

	def attachx(self,image,n,win):
		self.file_name = 'zoom'+str(n)+'.png'
		image.save(self.file_name)
		in_window(self.X/2,self.Y/2,self.file_name,win)
		
	def winBx(self,n):
		"""set coords for complex plane """
		if n==0:
			self.winB = GraphWin('select',self.X,self.Y)
			self.winB.master.geometry( '%dx%d+%d+%d' % (self.X,self.Y, 1.3*self.X, 35) )
		in_window(self.X/2,self.Y/2,'zoom'+str(n)+'.png',self.winB)
		self.complex_coords()

	def complex_coords(self,N,win):
		print('complex_coords')
		cx,cy,w = self.cx,self.cy,self.w
		win.setCoords(cx-w/2,cy-w/2,cx+w/2,cy+w/2)
		# self.show_coords(N,win)

	def show_coords(self,N,win):
		cx,cy,w = self.cx,self.cy,self.w
		Circle(Point(cx,cy),self.w/100).draw(win).setFill('blue')
		xmin,ymin = cx-w/2,cy-w/2
		s = w/N
		for i in range(N):
			for j in range(N):
				Rectangle(Point(xmin+i*s,ymin+j*s),Point(xmin+(i+1)*s,ymin+(j+1)*s)).draw(self.winA)

	def click_select(self,x,y,w):
		# w = width of current window
		N=5
		self.complex_coords(N,self.winA)
		clk = self.winA.getMouse()
		cx,cy = clk.x,clk.y

		s = w/(2*N)
		re = Rectangle(Point(cx-s,cy-s),Point(cx+s,cy+s)).draw(self.winA)
		# time.sleep(3)
		# re.undraw()
		return cx,cy,2*s

	def click_select3(self,xo,yo,w):
		print('click_select')
		"""have a center cx,cy set with coords
		click x,y relative to that, in coords given
		want x,y to become center dx,dy equal
		x-cx,y-cy worked with Zoom 3"""
		N=5
		self.complex_coords(N,self.winA)
		cx,cy = xo,yo
		clk = self.winA.getMouse()
		x,y = clk.x,clk.y

		# Circle(Point(x,y),w/100).draw(self.winA).setFill('red')
		# ci = Circle(Point(x,y),w/100).draw(self.winB).setFill('red')
		s = self.w/(2*N)
		re=Rectangle(Point(x-s,y-s),Point(x+s,y+s)).draw(self.winA)
		# Rectangle(Point(x-s,y-s),Point(x+s,y+s)).draw(self.winB)

		self.cx,self.cy = x,y

		time.sleep(2)
		re.undraw()
		return x,y,2*s  #side of selection box

	def click_select1(self):
		cx,cy,w = self.cx,self.cy,self.w
		print('\ncx,cy,w',cx,cy,w,'CLICK')

		clk = self.winA.getMouse()
		x,y = clk.x,clk.y
		print('x,y    ', round(x,4),round(y,4) )

		dx,dy = x-cx,y-cy
		print('dx,dy  ', round(dx,4),round(dy,4) )
		Line(Point(cx,cy),Point(x,y)).draw(self.winA).setArrow('last')
		x,y = cx+dx,cy+dy    
		# w = self.select_zoom_region(x,y)
		self.cx,self.cy = x,y
		return x,y,self.w

	def select_zoom_regionx(self,x,y):
		s1 = self.w / 4  # side of selection square / new w  (window size /4)
		s = s1/2
		# Circle(Point(x,y),self.w/10)

		# re = Rectangle(Point(x-s,y-s),Point(x+s,y+s)).draw(self.winA)
		# re.setOutline('orange')
		# re.setWidth(3)
		return s1  # selected region  (here w/4)

	def zoom_on_center(self,cx,cy,w):
		# hilight button
		xmin,ymin = cx-w/2,cy-w/2
		Circle(Point(xmin,ymin),w/8).draw(self.winB).setFill('magenta')
		# return center and w/2
		return cx,cy,w/2
		in_window(self.file_name,self.winB)	

if __name__=='__main__': 
	pass
	



	

	