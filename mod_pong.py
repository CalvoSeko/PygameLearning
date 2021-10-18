import pygame
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
pygame.display.set_caption("Pong")
# variables
font = pygame.font.Font('freesansbold.ttf', 32)

done = False
score = 0
ball_width = 20
x_val = 150
y_val = 200
x_direction = 2.0
y_direction = 2.0

padd_length = 15
padd_width = 60

x_padd = 0
y_padd = 20

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
 # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

 # -- Game logic goes after this comment
 # -- Screen background is BLACK
    screen.fill (black)
 # -- Draw here
    pygame.draw.rect(screen, pink, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen, moon_glow, (x_padd,y_padd,padd_length,padd_width))
 #change variables


    if y_padd <= y_val and y_padd + padd_width >= y_val and padd_length >= x_val:
        x_direction = x_direction * -1.25




    if x_val >= 630:
        x_direction = x_direction * -1
    if y_val >= 470:
        y_direction = y_direction * -1
    if y_val <= 10:
        y_direction = y_direction * -1

        ## - the up key or down key has been pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_padd >= 0:
        y_padd = y_padd - 5
     
    if keys[pygame.K_DOWN] and y_padd <= 480 - padd_width:
        y_padd = y_padd + 5

    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    if x_val <= 0:
        score = score + 1
        x_val = 150
        y_val = 200
        x_direction = 2.0
        y_direction = 2.0
    



 # -- flip display to reveal new position of objects
    pygame.display.flip()
 # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()