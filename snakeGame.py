# Snake Game

import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("ERRORS!".format(check_errors[1]))
    sys.exit(-1)
else:
    print("Initialized Successd!")

SIDE = 500

playSurface = pygame.display.set_mode((SIDE,SIDE))
pygame.display.set_caption("Sanke Game")

# Colors
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

# FPS controller
fpsController = pygame.time.Clock()

# Important varibles
snakePos = [SIDE/2, SIDE/2]
snakeBoady = [[SIDE/2, SIDE/2], [SIDE/2-10, SIDE/2], [SIDE/2-20, SIDE/2]]

foodPos = [random.randrange(1,SIDE/10)*10,random.randrange(1,SIDE/10)*10]
foddSpawn = True

direction = 'RIGHT'
changeto = direction

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    gameOverSurf = myFont.render('Game Over!', True, red)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (SIDE/2, 15)
    playSurface.blit(gameOverSurf,gameOverRect)
    pygame.display.flip()
    time.sleep(10)
    pygame.quit()
    sys.exit()
