# Flappy Bird game in python
# Author: Bhavya Patel
# Date: 07-29-2023
from turtle import width
import pygame
from pygame.locals import *

# Global variables & constants

# Initialize a window or screen for display
# Constant variables
# 1400 x 700 as these are the dimensions of background.png file, so that it covers entire screen
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# To make group of all images as dictionary
GAME_IMAGES = {}
# To make group of all audios as dictionary
GAME_SOUNDS = {}








# Functions








# Main Program

# Initialize pygame
pygame.init()

# Add all images as key value pairs to GAME_IMAGES dictionary

# Load images and to optimize images we use .convert_alpha() method
# storing it in a variable named background is efficient as
# now whenever we need to this image we can access it thought background variable
GAME_IMAGES["background"] =  pygame.image.load("image/background.png").convert_alpha()
GAME_IMAGES["base"] =  pygame.image.load("image/base.png").convert_alpha()
# Here our player is bird
GAME_IMAGES["player"] =  pygame.image.load("image/bird.png").convert_alpha()
GAME_IMAGES["message"] =  pygame.image.load("image/message.png").convert_alpha()
# Let's make a group for all numbers( 0 to 9 ):=> tuple
GAME_IMAGES["numbers"] = (
    pygame.image.load("image/0.png").convert_alpha(),
    pygame.image.load("image/1.png").convert_alpha(),
    pygame.image.load("image/2.png").convert_alpha(),
    pygame.image.load("image/3.png").convert_alpha(),
    pygame.image.load("image/4.png").convert_alpha(),
    pygame.image.load("image/5.png").convert_alpha(),
    pygame.image.load("image/6.png").convert_alpha(),
    pygame.image.load("image/7.png").convert_alpha(),
    pygame.image.load("image/8.png").convert_alpha(),
    pygame.image.load("image/9.png").convert_alpha()
)
# here we need 2 types of pipe
# 1 inverted vertical pipe
# 2 normal vertical pipe
GAME_IMAGES["pipe"] =  (
    # Upper pipe: Just give 180 degree rotation
    pygame.transform.rotate(pygame.image.load("image/pipe.png").convert_alpha(), 180),
    # Lower pipe
    pygame.image.load("image/pipe.png").convert_alpha()
)

# Add all audios as key value pairs to dictionary GAME_SOUNDS
GAME_SOUNDS["die"] = pygame.mixer.Sound("audio/die.mp3")
GAME_SOUNDS["fly"] = pygame.mixer.Sound("audio/fly.flac")
GAME_SOUNDS["point"] = pygame.mixer.Sound("audio/point.mp3")


