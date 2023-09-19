import pygame as pg
import math
from pygame import mixer
import random as r

pg.init()

screen_x_size = 800
screen_y_size = 600

screen = pg.display.set_mode((screen_x_size, screen_y_size))

pg.display.set_caption("Space Shooter Game")


mixer.music.load('./Spaceship/Sounds/game.mp3')
mixer.music.play(-1)

# icons
icon_img = pg.image.load('./Spaceship/img_downsized/icon.png')
ball_img = pg.image.load('./Spaceship/img_downsized/ball.png')
bullet_img = pg.image.load('./Spaceship/img_downsized/bullet_d.png')
enemy1_img = pg.image.load('./Spaceship/img_downsized/enemy1_d.png')
enemy2_img = pg.image.load('./Spaceship/img_downsized/enemy2_d.png')
player_img = pg.image.load('./Spaceship/img_downsized/player_d.png')
ball_img = pg.image.load('./Spaceship/img_downsized/ball.png')
space_big_img = pg.image.load('./Spaceship/img_downsized/space_d.png')
alien_blaster_img = pg.image.load('./Spaceship/img_downsized/alienblaster_d.png')
explosion_img = pg.image.load('./Spaceship/img_downsized/explosion.png')


font = pg.font.SysFont('Ariel', 32, 'bold')

pg.display.set_icon(icon_img)


spaceshipX = 370
spaceshipY = 480

enemy1X = r.randint(0, 736)
enemy1Y = 50
enemy1_changeX = 1
enemy1_changeY = 0
enemy1_ratio = 1

changeX = 0
changeY = 0
ratio = 30
steps_x = 0.2
steps_y = 0.2

ball_x = r.randint(0, screen_x_size)
ball_y = r.randint(0, screen_y_size)

def ball_pos(x, y):
    screen.blit(ball_img, (x, y))

def player():
    screen.blit(player_img, (spaceshipX, spaceshipY))

def enemy1():
    screen.blit(enemy1_img, (enemy1X, enemy1Y))

def process_event(event):
    global spaceshipX, spaceshipY, changeX, changeY, enemy1X, enemy1Y, enemy1_changeX, enemy1_changeY, enemy1_ratio

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            changeX = -1*ratio
        if event.key == pg.K_RIGHT:
            changeX = +1*ratio
        if event.key == pg.K_UP:
            changeY = -1*ratio
        if event.key == pg.K_DOWN:
            changeY = +1*ratio
    if event.type == pg.KEYUP:
        changeX = 0
        changeY = 0

    spaceshipX += changeX
    spaceshipY += changeY

    if spaceshipX < 0:
        spaceshipX = 0
    elif spaceshipX > 736:
        spaceshipX = 736
    if spaceshipY > 480:
        spaceshipY = 480
    elif spaceshipY < 30:
        spaceshipY = 30
   

is_active = True

while is_active:

    screen.blit(space_big_img, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_active = False
        process_event(event)

    enemy1X += enemy1_changeX * enemy1_ratio
    enemy1Y += enemy1_changeY

    if enemy1X < 0 or enemy1X > 726:
        enemy1_ratio *= -1
        enemy1Y += 20

    if enemy1Y > 480:
        enemy1Y = 480
    elif enemy1Y < 30:
        enemy1Y = 30


    player()
    enemy1()
    if ball_x > screen_x_size-10 or ball_x < 0:
        steps_x = -steps_x
    if ball_y > screen_y_size-10 or ball_y < 0:
        steps_y = -steps_y

    ball_x += steps_x
    ball_y += steps_y
    ball_pos(ball_x, ball_y)

    pg.display.update()
