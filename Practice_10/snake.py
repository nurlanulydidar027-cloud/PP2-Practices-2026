import pygame, random

pygame.init()
WIDTH = 500; HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

# настройки
CELL = 20
speed = 7
score = 0
level = 1

snake = [(100,100),(80,100),(60,100)]
direction = (CELL,0)
last_direction = direction  # добавим для отслеживания предыдущего направления

def random_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x,y) not in snake:
            return (x,y)

food = random_food()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",24)
running=True

while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # движение только в допустимых направлениях
            if event.key == pygame.K_UP and last_direction != (0, CELL):
                direction = (0,-CELL)
            if event.key == pygame.K_DOWN and last_direction != (0, -CELL):
                direction = (0,CELL)
            if event.key == pygame.K_LEFT and last_direction != (CELL, 0):
                direction = (-CELL,0)
            if event.key == pygame.K_RIGHT and last_direction != (-CELL, 0):
                direction = (CELL,0)

    # движение змейки
    head_x, head_y = snake[0]
    new_head = (head_x+direction[0], head_y+direction[1])

    # столкновение со стеной
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake):
        running = False

    snake.insert(0,new_head)

    if new_head == food:
        score += 1
        food = random_food()
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    last_direction = direction  # обновляем последнее направление

    screen.fill((0,0,0))
    for part in snake:
        pygame.draw.rect(screen,(0,255,0), pygame.Rect(part[0], part[1], CELL, CELL))
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(food[0],food[1],CELL,CELL))

    text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
    screen.blit(text,(10,10))

    pygame.display.flip()

pygame.quit()