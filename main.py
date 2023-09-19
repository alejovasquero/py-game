import pygame as pg
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

changeX = 0
changeY = 0
steps_x = 0.2
steps_y = 0.2

ball_x = r.randint(0, screen_x_size)
ball_y = r.randint(0, screen_y_size)

def ball_pos(x, y):
    screen.blit(ball_img, (x, y))

is_active = True

while is_active:

    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_active = False
    
    if ball_x > screen_x_size-10 or ball_x < 0:
        steps_x = -steps_x
    if ball_y > screen_y_size-10 or ball_y < 0:
        steps_y = -steps_y

    ball_x += steps_x
    ball_y += steps_y
    ball_pos(ball_x, ball_y)

    pg.display.update()
