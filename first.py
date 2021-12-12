import pygame
import random

#initialize the pygame
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800,600)) #800 = width, 600 = height

#the infinite loop will allow us to have the window open   
running = True

#Title and icon 
pygame.display.set_caption("First Game")
icon = pygame.image.load('png_logo/001-spaceship.png') #load the icon 
pygame.display.set_icon(icon) #apply the icon

#Player
playerImg = pygame.image.load('png_logo/001-spaceship.png')
playerX = 370
playerY = 480   

#Enemy
enemyImg = pygame.image.load('png/001-space-invaders.png')
enemyX = random.randint(0,764)
enemyY = random.randint(50,150)  

playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def test_func(speed):
    print(speed)

a = 97
d = 100
w = 119
s = 115

holding_a = False
holding_d = False
holding_s = False
holding_w = False

ship_speed = 0.15

#Game loop
while running:
    #every time that the cicle repeats the screen will be cleared
    #if we do not clear the screen, the image will be scaling  
    screen.fill((0,0,0)) #fill the screen with black

    for event in pygame.event.get(): # this will get the events from the window
        if event.type == pygame.QUIT:
            running = False
        #keyborad events 
        #width     
        if event.type == pygame.KEYDOWN and event.key == a:
            playerX_change = -ship_speed
            holding_a = True
        if event.type == pygame.KEYDOWN and event.key == d:
            playerX_change = ship_speed
            holding_d = True
        #height    
        if event.type == pygame.KEYDOWN and event.key == w:
            playerY_change = -ship_speed
            holding_w = True
        if event.type == pygame.KEYDOWN and event.key == s:
            playerY_change = ship_speed
            holding_s = True

        #if we stop holding a key then the ship stop moving
        if event.type == pygame.KEYUP:
            #width
            if event.key == a:
                holding_a = False
                playerX_change = 0
            if event.key == d:
                holding_d = False
                playerX_change = 0    
            
            #height
            if event.key == s:
                holding_s = False
                playerY_change = 0
            if event.key == w:
                holding_w = False
                playerY_change = 0

        #if we are holding two keys and we realese one, the ship will move to the key that is True
        #if we are holding two keys then ship will move to the most recent pressed key
        if holding_a == True and holding_d == False: # width
            playerX_change = -ship_speed
        if holding_a == False and holding_d == True:
            playerX_change = ship_speed

        if holding_s == True and holding_w == False: #height
            playerY_change = ship_speed
        if holding_s == False and holding_w == True:
            playerY_change = -ship_speed
            
    #apply changes            
    playerX += playerX_change
    playerY += playerY_change

    #limits
    if playerX <= 0:
        print('this is a limit')
        playerX = 0
    elif playerX >= 764:
        print('this is a limit')
        playerX = 764
    if playerY <= 0:
        print('this is a limit')
        playerY = 0
    elif playerY >= 564:
        print('this is a limit')
        playerY = 564 
    player(playerX,playerY) #call the player function
    enemy(enemyX,enemyY)
    pygame.display.update() #update the screen