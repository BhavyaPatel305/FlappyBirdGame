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

# Coordinates of bird
playerX = SCREEN_WIDTH/5
playerY = SCREEN_HEIGHT/2










# Functions
# Method to display welcome screen
def welcomeScreen():
    # Now since when we run this file, a screen appears for a second and then disappears
    # So to prevent that, we will use an infinite while loop
    while True:
        # 1 Background
        SCREEN.blit(GAME_IMAGES["background"], (0,0))

        # 2 Base
        SCREEN.blit(GAME_IMAGES["base"], (baseX, baseY))

        # 3 bird
        SCREEN.blit(GAME_IMAGES["player"], (playerX, playerY))

        # 4 Message
        SCREEN.blit(GAME_IMAGES["message"], (messageX, messageY))


        # nothing would be seen on screen if we dont write this: pygame.display.update()
        pygame.display.update()





# Main Program

# Initialize pygame
pygame.init()

# Set the caption of game window
pygame.display.set_caption("Flappy Bird")

# Add all images as key value pairs to GAME_IMAGES dictionary

# Load images and to optimize images we use .convert_alpha() method
# storing it in a variable named background is efficient as
# now whenever we need to this image we can access it thought background variable
GAME_IMAGES["background"] =  pygame.image.load("images/background.png").convert_alpha()
GAME_IMAGES["base"] =  pygame.image.load("images/base.png").convert_alpha()
# Here our player is bird
GAME_IMAGES["player"] =  pygame.image.load("images/bird.png").convert_alpha()
GAME_IMAGES["message"] =  pygame.image.load("images/message.png").convert_alpha()
# Let's make a group for all numbers( 0 to 9 ):=> tuple
GAME_IMAGES["numbers"] = (
    pygame.image.load("images/0.png").convert_alpha(),
    pygame.image.load("images/1.png").convert_alpha(),
    pygame.image.load("images/2.png").convert_alpha(),
    pygame.image.load("images/3.png").convert_alpha(),
    pygame.image.load("images/4.png").convert_alpha(),
    pygame.image.load("images/5.png").convert_alpha(),
    pygame.image.load("images/6.png").convert_alpha(),
    pygame.image.load("images/7.png").convert_alpha(),
    pygame.image.load("images/8.png").convert_alpha(),
    pygame.image.load("images/9.png").convert_alpha()
)
# here we need 2 types of pipe
# 1 inverted vertical pipe
# 2 normal vertical pipe
GAME_IMAGES["pipe"] =  (
    # Upper pipe: Just give 180 degree rotation
    pygame.transform.rotate(pygame.image.load("images/pipe.png").convert_alpha(), 180),
    # Lower pipe
    pygame.image.load("images/pipe.png").convert_alpha()
)

# Add all audios as key value pairs to dictionary GAME_SOUNDS
GAME_SOUNDS["die"] = pygame.mixer.Sound("audio/die.mp3")
GAME_SOUNDS["fly"] = pygame.mixer.Sound("audio/fly.flac")
GAME_SOUNDS["point"] = pygame.mixer.Sound("audio/point.mp3")

# Pasting images on screen is called Blit in technical terms
# it is important to maintain the order in which we paste images on screen
# say if 1st i paste small bird image on screen and then paste big background image
# then we would not be able to see the bird

# Coordinates of Base
baseX = 0
baseY = SCREEN_HEIGHT - GAME_IMAGES["base"].get_height()

# Coordinates of message
messageX = SCREEN_WIDTH/2 - GAME_IMAGES["message"].get_width()/2
messageY = SCREEN_HEIGHT/2 - GAME_IMAGES["message"].get_height()/2

# Call welcomeScreen() method to display welcome message
welcomeScreen()


