import pygame
from ball import Ball
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

vel = [10, 0.01]
vel2 = [4, 0.01]
vel3 = [-6, 0.01]
gravity = 0.3
balls: list[Ball] = []
b = Ball(400, 100, 8, 40, (255, 255, 0), vel)
b2 = Ball(200, 20, 400, 20, (255, 0, 0), vel2)
b3 = Ball(600, 40, 10, 30, (255, 0, 255), vel3)
balls.append(b)
balls.append(b2)
balls.append(b3)

def check_collision(ball: Ball):
    # floor collision
    if ball.y + ball.radius > 600:
        ball.y = 600 - ball.radius
        ball.scale_velo(1, -0.8)
        if abs(ball.get_velo()[1]) < 0.5:
            ball.set_velo(ball.get_velo()[0], 0)
    
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
    distance = ((b1.x - b2.x)**2 + (b1.y - b2.y)**2) ** 0.5
    if distance <= b1.radius + b2.radius:
        v1x, v1y = b1.get_velo()
        v2x, v2y = b2.get_velo()
        b1.velo[0] = calc_final_velo(b1.mass, b2.mass, v1x, v2x)
        b2.velo[0] = calc_final_velo(b2.mass, b1.mass, v2x, v1x)
        b1.velo[1] = calc_final_velo(b1.mass, b2.mass, v1y, v2y)
        b2.velo[1] = calc_final_velo(b2.mass, b1.mass, v2y, v1y)

def calc_final_velo(m1, m2, v1, v2):
    return ((2 * m2 * v2) + m1 * v1 - m2 * v1) / (m1 + m2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                b.y = random.randint(50, 200)
                b2.y = random.randint(50, 200)
                b3.y = random.randint(50, 200)
                if random.choice([True, False]):
                    b.velo[0] = random.randint(70, 100)
                else:
                    b.velo[0] = random.randint(-10, -7)

                if random.choice([True, False]):
                    b2.velo[0] = random.randint(7, 10)
                else:
                    b2.velo[0] = random.randint(-10, -7)
                
                if random.choice([True, False]):
                    b3.velo[0] = random.randint(70, 100)
                else:
                    b3.velo[0] = random.randint(-10, -7)
            if event.key == pygame.K_w:
                if abs(b.get_velo()[1]) < 0.5:
                    b.velo[1] += -10

    
    screen.fill((0, 0, 0))  # clear screen
    # draw things here

    for ball in balls:
        ball.move()
        check_collision(ball)

    check_ball_collision(b, b2)
    check_ball_collision(b, b3)
    check_ball_collision(b2, b3)

    if b.velo != 0:
        b.add_to_velo(0, gravity)

    if b2.velo != 0:
        b2.add_to_velo(0, gravity)
    
    if b3.velo != 0:
        b3.add_to_velo(0, gravity)

    b.draw(screen)
    b2.draw(screen)
    b3.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()