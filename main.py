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
# Number of frames per second
# If a lot of frames pass though in front of our eyes then we think that it is moving smoothly
# But more the FPS, more load on computer
# but if load on computer less than game experience will be bad
FPS = 30

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
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/0.6, "y": newPipe3[0]["y"]},
    ]
    
    # List of lower pipes
    lowerPipes = [
        {"x": SCREEN_WIDTH, "y": newPipe1[1]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/3, "y": newPipe2[1]["y"]},
        {"x": SCREEN_WIDTH + SCREEN_WIDTH/0.6, "y": newPipe3[1]["y"]},
    ]
    
    # variable to store score of the player
    score = 0
    
    # speed with which pipes would be moving towards bird on x-axis
    pipeSpeedX = -10
    
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
    
    # Coordinates of bird
    # We define it once again as it gives error or we can even use global keyword
    playerX = SCREEN_WIDTH/5
    playerY = SCREEN_HEIGHT/2
    
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
        # But by just changing speed, we cannot move the bird
        # We need to write logic for that
        
        # Moving player up
        
        playerY = playerY + playerSpeedY
        # If we press ^ arrow key once, then playerFlying = True
        # Now we set it to false as we have added playerSpeedY once
        # so now once again set it to false, as we don't want it to keep flying
        if playerFlying == True:
            playerFlying = False
            
        # Pulling player down
        
        # If playerSpeedY is less than its max possible speed and it is not flying right now
        # then pull it down
        if (playerSpeedY < playerMaxSpeed) and not playerFlying:
            # We add acc to player speed, so it comes down
            playerSpeedY = playerSpeedY + playerAccY
            
        # Moving the pipes
        
        # for this we will use zip function
        for upperPipe,lowerPipe in zip(upperPipes, lowerPipes):
            # We add pipeSpeedX as it is a negative value
            upperPipe["x"] = upperPipe["x"] + pipeSpeedX
            lowerPipe["x"] = lowerPipe["x"] + pipeSpeedX
            
        # Adding new pipes
        # When to add new pipe
        # If we don't use pipeSpeedX here than on increasing pipe's speed, game will not work properly
        # we use abs() method as pipeSpeedX is negative
        if 0 < upperPipes[0]["x"] <= abs(pipeSpeedX):
            newPipe = getRandomPipes()
            # from the newly generated pipe add its inverted(upper part) to upperPipes list
            upperPipes.append(newPipe[0])
            # from the newly generated pipe add its vertical(lower part) to lowerPipes list
            lowerPipes.append(newPipe[1])
            
        # Removing old pipes
        # if pipe has already crossed the left most end of screen than pop that pipe from list
        if upperPipes[0]["x"] < 0:
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Changing the score
        # Here we ue the logic that if center if bird passes ahead of center of pipe then we increment the score
        # To get center: Current x coordinate of bird + (Width of bird)/2
        playerCenterX = playerX + (GAME_IMAGES["player"].get_width()/2)
        
        # Similarly we find pipe center
        # But we use for loop to check center for each and every pipe
        for pipe in upperPipes:
            pipeCenterX = pipe["x"] + (GAME_IMAGES["pipe"][0].get_width()/2)
            
            if pipeCenterX <= playerCenterX < pipeCenterX + abs(pipeSpeedX):
                score += 1
                # Play point sound which signifies that score has increased
                GAME_SOUNDS["point"].play()
                
        # Player Death
        # die variable stores a boolean value, if player dead or not
        if isHit(playerX, playerY, upperPipes, lowerPipes):
            # If bird dies, play die sound
            GAME_SOUNDS["die"].play()
            # After playing sound, wait for sometime
            pygame.time.wait(2000)
            # After that return, it means that it will go where gameLoop() method was called 
            return        
        
        # Blit on screen
        
        # 1 Background
        SCREEN.blit(GAME_IMAGES["background"], (0,0))

        # 3 bird
        SCREEN.blit(GAME_IMAGES["player"], (playerX, playerY))
        
        # Let's blit the pipes on screen
        for upperPipe,lowerPipe in zip(upperPipes, lowerPipes):
            # blit the upper pipe(Inverted pipe)
            SCREEN.blit(GAME_IMAGES["pipe"][0], (upperPipe["x"], upperPipe["y"]))
            # blit the lower pipe(Vertical pipe)
            SCREEN.blit(GAME_IMAGES["pipe"][1], (lowerPipe["x"], lowerPipe["y"]))
        
        # 2 Base
        # We print base afterwards so that pipes does not get placed on top of base
        SCREEN.blit(GAME_IMAGES["base"], (baseX, baseY))
        
        # Blit the score
        scoreDigits = [int(i) for i in str(score)]
        # Coordinates of score, like at which position to blit the score
        scoreX = SCREEN_WIDTH/1.3
        scoreY = SCREEN_HEIGHT/2
        # start blitting the score on the screen
        for digit in scoreDigits:
            SCREEN.blit(GAME_IMAGES["numbers"][digit], (scoreX,scoreY))
            # Lets say score is 123
            # so first 1 is printed, then we increment scoreX by the width of the digit being blit
            # so that 2 will not be printed on top of 1, it will be printed after 1
            scoreX += GAME_IMAGES["numbers"][digit].get_width()
        
        # update the screen
        pygame.display.update()
        
        # implementing FPS
        # By passing this command, pygame understands that it has to pass these many frames
        pygame.time.Clock().tick(FPS)
    
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
    
# Method to check if our player has hit pipes or not
# returns True if the player has hit else False
def isHit(playerX, playerY, upperPipes, lowerPipes):  
     # Get the height of the pipe image
    pipeHeight = GAME_IMAGES["pipe"][0].get_height()
    # Get the width of the pipe image
    pipeWidth = GAME_IMAGES["pipe"][0].get_width()
    # Get the height of the player image
    playerHeight = GAME_IMAGES["player"].get_height()
    # Get the width of the player image
    playerWidth = GAME_IMAGES["player"].get_width()
    
    # 1: HIT CEILING OR BASE
    
    # Which means y coordinate of player < 0 or it goes below the base
    # here y coordinate is the upper left corner of bird image
    # But for checking collision with base, we want to check for lower left corner of bird image
    # so we add bird height to it's y coordinate
    if playerY < 0 or (playerY + playerHeight) >= (SCREEN_HEIGHT - GAME_IMAGES["base"].get_height()):
        return True
    
    # 2: HIT WITH UPPER PIPES
    for pipe in upperPipes:
        # Take pipe's y coordinate and add pipe height to it
        if (playerY < pipe["y"] + pipeHeight) and ((pipe["x"] - playerWidth) < playerX < (pipe["x"] + pipeWidth)):
            return True
        
    # 3: HIT WITH LOWER PIPES
    for pipe in lowerPipes:
        # Take pipe's y coordinate and add pipe height to it
        if (playerY + playerHeight > pipe["y"]) and ((pipe["x"] - playerWidth) < playerX < (pipe["x"] + pipeWidth)):
            return True
    
    # 4: DIDN'T HIT ANYTHING
    return False
        
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

# If gameLoop finishes, it will again go back to welcome screen
while True:
    # Call welcomeScreen() method to display welcome message
    welcomeScreen()
    # Method that contains all the logic of the game
    # Like with what speed bird will fly, how many pipes would come, what would be distance between each pipe
    gameLoop()