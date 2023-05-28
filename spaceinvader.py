import pygame
import time
import random
import math

pygame.init()#initialise pygame

#creating screen
screen=pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("space invaders")
icon=pygame.image.load("foxy.jpg")
bullet=pygame.image.load("bullet.png")
pygame.display.set_icon(icon)

#player
playerimg=pygame.image.load("player.png")
playerX=370
playerY=480
playerx_change=0

#bullet
#ready-cant see bullet on screen
#fire-bullet is moving
bulletimg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bullety_change=20
bullet_state="ready"

#multiple enemies
enemyimg=[]
enemyX=[]
enemyY=[]
enemyy_change=[]
enemyx_change=[]
num_enemies=6

for i in range(num_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyx_change.append(10)
    enemyy_change.append(0)


#score
score_val=0
font=pygame.font.Font('freesansbold.ttf',32)
#game over
over_font = pygame.font.Font('freesansbold.ttf', 32)


#draw on screen
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Oh no! the enemy came too close", True, (255, 255, 255))
    screen.blit(over_text, (150, 250))
    over_text2 = over_font.render("Game Over!!", True, (255, 255, 255))
    screen.blit(over_text2, (250, 280))
    # time.sleep(3)
    # exit()

    




#game loop
running =True
while running:
    for event in pygame.event.get():#looping through all the events
        if event.type == pygame.QUIT:
            running =False


        #checking if any keystroke is pressed
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-10
            if event.key==pygame.K_RIGHT:
                playerx_change=10
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    fire(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0
        
            


    # playerX+=0.1
    #we want out bg to be there always so we write command for bg in while loop
    # screen.fill((0,0,0))#in a tuple
    backGround=pygame.image.load("bg.jpg")
    screen.blit(backGround,(0,0))   


    playerX+=playerx_change


#checking for boundaries
    if playerX<=0:
        playerX=0 
    elif playerX>=730:
        playerX=730


    for i in range(num_enemies):
        enemyX[i]+=enemyx_change[i]

        if enemyY[i]>400:
            for j in range(num_enemies):
                enemyY[j]=1000

            game_over_text()

        if enemyX[i]<=0 or enemyX[i]>=730:
            enemyx_change[i]*=-1
            enemyY[i]+=40

    #checking for collision with enemy
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            score_val+=1

            enemy(enemyX[i], enemyY[i],i)

#bullet moving after fired
    if bullet_state is "fire":
        fire(bulletX,bulletY)
        bulletY-=bullety_change
        if bulletY<=0:
            bullet_state="ready"
            bulletX=0
            bulletY=480



    player(playerX,playerY)


    for i in range(num_enemies):
        enemy(enemyX[i],enemyY[i],i)

    show_score(10,10)
    pygame.display.update()
