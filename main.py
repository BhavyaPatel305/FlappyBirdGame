# Flappy Bird game in python
# Author: Bhavya Patel
# Date: 07-29-2023
from turtle import width
import pygame
from pygame.locals import *
# used to stop program from running when pressed esc key
import sys
# used to generate random coordinates for pipes
from random import randint

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
        
        # Whenever our bird collides with ground or we press some key, all those things are stored in pygame as events
        # we use get keyword to get those events
        # data type of those events that we get using get method is LIST: []
        # So this list stored events like a key press etc inside of it
        # So we fetch each and every event from list and check if we pressed say esc key
        for x in pygame.event.get():
            # If type of x is keydown, meaning some key was pressed
            # and that key is esc key(In pygame we use K_ESCAPE for esc key)
            # if any where we get error like something is not callable, meaning we have put some extra () some where
            if x.type == KEYDOWN and x.key == K_ESCAPE:
                # if esc key pressed, then quit pygame
                pygame.quit()
                # But using pygame.quit() we are just closing pygame, but our program is still calling pygame
                # so to stop program from calling pygame we use sys.exit() to stop the program
                sys.exit()
            # If user presses space bar, then start the game
            if x.type == KEYDOWN and x.key == K_SPACE:
                # Simply return, because just after welcomeScreen function we are calling gameLoop() method
                return

# Method that contains all the logic of the game
# Like with what speed bird will fly, how many pipes would come, what would be distance between each pipe
def gameLoop():
    # 1st we need to create pipes
    # Say 1 pipe is combination of 1 vertical and 1 inverted pipe
    # Lets create 3 such pipes
    # We create a method named getRandomPipe() which will give us random pair of pipes
    newPipe1 = getRandomPipes()
    newPipe2 = getRandomPipes()
    newPipe3 = getRandomPipes()
    
    # We make these 2 separate list of upper and lower pipes to recognize bird collision with a pipe
    
    # List of inverted Pipes/upper pipes, used to store this part: {"x": pipeX, "y": y1} for each of the 3 new pipes
    # Now we dont want all 3 upper pipes to start from same position, SCREEN_WIDTH as if we do that we will only see 1 inverted pipe and not 3
    # so we leave some space between each pipe on x axis
    upperPipes = [
        {"x": SCREEN_WIDTH, "y": newPipe1[0]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/3, "y": newPipe2[0]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/0.75, "y": newPipe3[0]["y"]},
    ]
    
    # List of lower pipes
    lowerPipes = [
        {"x": SCREEN_WIDTH, "y": newPipe1[1]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/3, "y": newPipe2[1]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/0.75, "y": newPipe3[1]["y"]},
    ]
    
    # variable to store score of the player
    score = 0
    
    # speed with which pipes would be moving towards bird on x-axis
    pipeSpeedX = -5
    
    # Speed with which bird would fall down or in other words, also called Gravity or Speed in y direction
    playerSpeedY = -9
    
    # Maximum speed of the player
    playerMaxSpeed = 10
    
    # Speed with which bird would fly
    playerFlyingSpeed = -8
    
    # so basically when we press ^ arrow key: it is the difference of 
    # playerGravityY - playerFlyingSpeed that decides how much bird will go up
    
    # Acceleration of player
    playerAccY = 1
    
    # boolean variable to check if player is flying or not
    playerFlying = False
    
    # height of the pipe
    pipeHeight = GAME_IMAGES["pipe"][0].get_height()
    
    # If I press ^ arrow or w, the player should move upwards
    while True:
        for x in pygame.event.get():
                # If press esc button, then close the game
                if x.type == KEYDOWN and x.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # If I press ^ key or w then player will go up
                if x.type == KEYDOWN and (x.key == K_UP or x.key == K_w):
                    # We want to fly and increase bird height only till it reaches top of the screen
                    # other wise it will go outside of the screen
                    if playerY > 0:
                        playerSpeedY = playerFlyingSpeed
                        playerFlying = True
                        # Along with flying, also play sound of flying
                        GAME_SOUNDS["fly"].play()
        # Blit on screen
        
        # 1 Background
        SCREEN.blit(GAME_IMAGES["background"], (0,0))

        # 2 Base
        SCREEN.blit(GAME_IMAGES["base"], (baseX, baseY))

        # 3 bird
        SCREEN.blit(GAME_IMAGES["player"], (playerX, playerY))
    
        # update the screen
        pygame.display.update()
        
    
    

# We create a method named getRandomPipe() which will give us random pair of pipes
def getRandomPipes():
    # gap variable is the gap between 1 vertical and 1 inverted pipe
    # We decide that the gap should be 3*height of bird
    # Using this we can control difficulty level
    # If you want to increase difficulty level, then reduce gap
    gap = GAME_IMAGES["player"].get_height()*3
    # Now lets generate coordinates of 1 vertical pipe(not the inverted one)
    # lets call the coordinates of vertical pipe x2,y2
    # MINIMUM height of the vertical pipe should be gap
    # as say we dont have any inverted pipe, then we need minumum gap for bird to go through
    # and then starts the vertical pipe after gap, till start of base
    y2 = randint(gap,SCREEN_HEIGHT - GAME_IMAGES["base"].get_height())
    
    
    # Lets define y1, that is y coordinate of inverted pipe
    # so for that lets say there is no vertical pipe, then
    # starting from base we go in negative y direction and leave a space = gap
    # after gap we start the inverted pipe
    # but we need to give coordinats of top left corner of inverted pipe image
    # so say y coordinate of base is 600
    # and say gap = 200
    # we go in negative y direction
    # so inverted pipe starts from 600 - 200 = 400(y-axis)
    # then to give top left corner coordinates of inverted pipe
    # we subtract height of inverted pipe image from 400 as we are going in negative y direction
    # we name it y1
    # here we start from y2 as say if there is no vertical pipe than y2 = base, and if there is then it will automatically leave a space = gap in between 2 pipes as y2 will be randomly generated
    # so accordingly y1 will be adjusted
    y1 = y2 - gap - GAME_IMAGES["pipe"][0].get_height()
    
    
    # Lets work on x - coordinates
    # We want to generate pipe outside screen on right side and move pipes slowly towards left, generating an illusion that bird is moving towards pipes
    # x coordinate of both the pipes will be same
    pipeX = SCREEN_WIDTH
    
    # now lets generate a pair of pipes
    pipe = [
        # Inverted Pipe
        {"x": pipeX, "y": y1},
        # Vertical Pipe
        {"x": pipeX, "y": y2}
    ]
    return pipe
    
    
    
    

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
# Method that contains all the logic of the game
# Like with what speed bird will fly, how many pipes would come, what would be distance between each pipe
gameLoop()

