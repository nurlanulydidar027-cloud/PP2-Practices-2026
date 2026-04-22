import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инструменты
colors = {
    pygame.K_r: RED,  # Красный
    pygame.K_g: GREEN,  # Зеленый
    pygame.K_b: BLUE,  # Синий
    pygame.K_k: BLACK,  # Черный
}

screen.fill(WHITE)
drawing = False
tool = "brush"  # Начальный инструмент — кисть
color = BLACK  # Начальный цвет — черный
last_pos = None

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Мышь
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Выбор цвета и инструментов
        if event.type == pygame.KEYDOWN:
            if event.key in colors:
                color = colors[event.key]  # Смена цвета кисти
            if event.key == pygame.K_e:
                tool = "eraser"  # Ластик
            if event.key == pygame.K_p:
                tool = "brush"  # Кисть
            if event.key == pygame.K_c:
                tool = "circle"  # Круг
            if event.key == pygame.K_r:
                tool = "rectangle"  # Прямоугольник
            if event.key == pygame.K_k:  # Переход обратно к черному цвету
                color = BLACK

    if drawing and last_pos:
        x, y = pygame.mouse.get_pos()

        if tool == "brush":
            pygame.draw.line(screen, color, last_pos, (x, y), 5)  # Рисуем линию
        elif tool == "eraser":
            # Ластик рисует белую линию для стирания
            pygame.draw.line(screen, WHITE, last_pos, (x, y), 15)  # Толщина ластика 15 пикселей
        elif tool == "rectangle":
            start = pygame.mouse.get_pos()
            w = pygame.mouse.get_rel()[0]
            h = pygame.mouse.get_rel()[1]
            pygame.draw.rect(screen, color, (x, y, 10, 10))
        elif tool == "circle":
            pygame.draw.circle(screen, color, (x, y), 10)

        last_pos = (x, y)  # Обновляем позицию

    pygame.display.flip()
    clock.tick(60)

pygame.quit()