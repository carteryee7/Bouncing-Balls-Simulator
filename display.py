import pygame
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

vel = [0, 0]
gravity = 0.3
ball = Ball(400, 20, 20, (255, 255, 0), vel)
stopped = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # clear screen
    # draw things here
    
    ball.move()

    if ball.y + ball.radius > 600:
        ball.y = 600 - ball.radius
        vel[1] *= -0.8
        if abs(vel[1]) < 0.5:
            vel[1] = 0
            stopped = True

    if not stopped:
        vel[1] += gravity

    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()