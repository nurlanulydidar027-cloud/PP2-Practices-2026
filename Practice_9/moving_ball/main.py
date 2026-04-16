import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
move_step = 20

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - move_step - ball_radius >= 0:
                    ball_y -= move_step
            elif event.key == pygame.K_DOWN:
                if ball_y + move_step + ball_radius <= HEIGHT:
                    ball_y += move_step
            elif event.key == pygame.K_LEFT:
                if ball_x - move_step - ball_radius >= 0:
                    ball_x -= move_step
            elif event.key == pygame.K_RIGHT:
                if ball_x + move_step + ball_radius <= WIDTH:
                    ball_x += move_step

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()