from image import *

pic = Picture('../pictures/bird.png')

pic.flipHorizontal()
pic.grayscale()
pic.rotateLeft()

pic.save_image("output.png")
