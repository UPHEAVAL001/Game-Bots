from PIL import ImageOps
import pyscreenshot as ImageGrab
import pyautogui as pg
import time
from numpy import *


class coordinates():
	replaybtn = (396,448)
	dinosaur = (234,466)
	obj = (270,461)




def resetgame():
	pg.click(coordinates.replaybtn)
	pg.keyDown('down')


def jump():
	pg.keyUp('down')
	pg.keyDown('space')
	print("jump")
	time.sleep(0.18)
	pg.keyUp('space')
	pg.keyDown('down')



def imageGrab():                                                                                    
	box = (coordinates.dinosaur[0]+36,coordinates.dinosaur[1],coordinates.dinosaur[0]+216,coordinates.dinosaur[1]+5)
	image = ImageGrab.grab(box)   
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	print(a.sum())  
	return a.sum() 
 




def main():
	resetgame()
	while True:
		if (imageGrab()!=1485):
			jump() 
			time.sleep(0.1)



main()     