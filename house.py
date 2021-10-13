import pygame
from time import sleep
# -- Global Constants
# -- Colours
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("House")
# -- Variable delaration
done = False
sun_x = 0
sun_y = 480
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
 # -- User input and controls
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
#End If
 #Next event
 # -- Game logic goes after this comment
 # -- Screen background is BLACK
 
 if sun_y <= 600:
     screen.fill(sky_blue)
 else:
     screen.fill(navy_blue)
 # -- Draw here
 
 pygame.draw.circle(screen, dandilion_yellow, (sun_x, sun_y),40,0)
 pygame.draw.rect(screen, lime, (0,280,640,200))
 #house
 pygame.draw.rect(screen, tan, (220,165,200,150))
 pygame.draw.rect(screen, light_gray, (320,235,40,80))
 
 sun_x = sun_x + 2
 sun_y = 1/500*(sun_x-320)**2

 if sun_y >= 750:
     sleep(3)
     sun_x = -40


 # -- flip display to reveal new position of objects
 pygame.display.flip()
 # - The clock ticks over
 clock.tick(60)
#End While - End of game loop
pygame.quit()
