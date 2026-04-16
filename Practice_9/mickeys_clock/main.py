import pygame
import sys
import math
import time

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

CENTER = (WIDTH // 2, HEIGHT // 2)

# Цвета
BLACK = (0, 0, 0)
RED = (220, 30, 30)
WHITE = (255, 255, 255)

# Загружаем фон (Микки)
clock_face = pygame.image.load("image/clock_face.jpg").convert()
clock_face = pygame.transform.smoothscale(clock_face, (WIDTH, HEIGHT))


def draw_hand(angle_deg, length, width, color):
    """Рисуем стрелку из центра по углу"""
    # -90 потому что 0° должно быть наверху (к 12)
    angle_rad = math.radians(angle_deg - 90)
    end_x = CENTER[0] + math.cos(angle_rad) * length
    end_y = CENTER[1] + math.sin(angle_rad) * length
    # Основная линия стрелки
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)
    # "Перчатка Микки" на конце (кружок)
    pygame.draw.circle(screen, WHITE, (int(end_x), int(end_y)), width + 3)
    pygame.draw.circle(screen, color, (int(end_x), int(end_y)), width + 3, 2)


# Главный цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Текущее время
    now = time.localtime()
    minutes = now.tm_min
    seconds = now.tm_sec

    # Углы (360/60 = 6° на одно деление)
    minute_angle = minutes * 6 + seconds * 0.1
    second_angle = seconds * 6

    # Рисуем фон
    screen.blit(clock_face, (0, 0))

    # Минутная стрелка (правая рука) — чёрная, толстая
    draw_hand(minute_angle, 200, 8, BLACK)

    # Секундная стрелка (левая рука) — красная, тонкая
    draw_hand(second_angle, 230, 4, RED)

    # Центральный круг
    pygame.draw.circle(screen, BLACK, CENTER, 10)
    pygame.draw.circle(screen, RED, CENTER, 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()