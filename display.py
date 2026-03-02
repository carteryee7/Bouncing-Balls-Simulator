import pygame
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

vel = [4, 0]
vel2 = [4, 0]
gravity = 0.3
b = Ball(400, 20, 20, (255, 255, 0), vel)
b2 = Ball(200, 20, 20, (255, 0, 0), vel2)
stopped = False

def check_collision(ball: Ball):
    # floor collision
    if ball.y + ball.radius > 600:
        ball.y = 600 - ball.radius
        ball.scale_velo(1, -0.8)
        if abs(ball.get_velo()[0]) < 0.5:
            ball.set_velo(ball.get_velo()[0], 0)
            stopped = True
    
    # ceiling collision
    if ball.y - ball.radius <= 0:
        ball.y = ball.radius
        ball.scale_velo(1, -1)
    
    # wall collision
    if ball.x + ball.radius >= 800:
        ball.x = 800 - ball.radius
        ball.scale_velo(-0.8, 1)
    
    # wall collision
    if ball.x - ball.radius <= 0:
        ball.x = ball.radius
        ball.scale_velo(-0.8, 1)

def check_ball_collision(b1: Ball, b2: Ball):
    rad = max(b.radius, b2.radius)
    if (abs(b1.x - b2.x) <= 2 * rad) and (abs(b.y - b2.y) <= 2 * rad):
        b.velo[0] *= -1
        b.velo[1] *= -1
        b2.velo[0] *= -1
        b2.velo[1] *= -1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # clear screen
    # draw things here
    
    b.move()
    b2.move()

    check_collision(b)
    check_collision(b2)

    check_ball_collision(b, b2)

    if not stopped:
        b.add_to_velo(0, gravity)
        b2.add_to_velo(0, gravity)

    b.draw(screen)
    b2.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()