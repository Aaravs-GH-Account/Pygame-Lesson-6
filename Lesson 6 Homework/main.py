import pygame,time
pygame.init()

screen=pygame.display.set_mode((500,500))

background=pygame.image.load('background.png')
player=pygame.image.load('bunny.png')

player_x=100
player_y=10

keys=[False,False,False,False]

while player_y<400:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_UP:
                keys[0]=True

            if event.key==pygame.K_DOWN:
                keys[2]=True

            if event.key==pygame.K_LEFT:
                keys[1]=True

            if event.key==pygame.K_RIGHT:
                keys[3]=True

        if event.type==pygame.KEYUP:

            if event.key==pygame.K_UP:
                keys[0]=False

            if event.key==pygame.K_DOWN:
                keys[2]=False

            if event.key==pygame.K_LEFT:
                keys[1]=False

            if event.key==pygame.K_RIGHT:
                keys[3]=False

    #up
    if keys[0]:
        if player_y > 0:
            player_y -= 7

    #down
    if keys[2]:
        if player_y < 400:
            player_y += 7

    #left
    if keys[1]:
        if player_x > 0:
            player_x -= 7

    #right
    if keys[3]:
        if player_x < 400:
            player_x +=7

    player_y +=5
    time.sleep(0.05)

print('Game Over!')