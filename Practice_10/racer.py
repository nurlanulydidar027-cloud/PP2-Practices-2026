import pygame, random
import os

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# игрок (машинка)
player = pygame.Rect(180, 500, 40, 60)
player_speed = 7

# монеты
coins = []
coin_timer = pygame.USEREVENT + 1
pygame.time.set_timer(coin_timer, 1500)
score = 0
font = pygame.font.SysFont("Arial", 30)

# рекорд
record_file = "highscore.txt"
if os.path.exists(record_file):
    with open(record_file, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

# настройка сложности
difficulty_multiplier = 1

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == coin_timer:
            if score // 10 > difficulty_multiplier:
                difficulty_multiplier += 1
                pygame.time.set_timer(coin_timer, 1500 - difficulty_multiplier * 200)  # уменьшаем интервал
            x = random.randint(0, WIDTH - 20)
            coins.append(pygame.Rect(x, -20, 20, 20))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    # обновление монет
    for coin in coins:
        coin.y += 4
        if coin.colliderect(player):
            score += 1
            coins.remove(coin)
        elif coin.y > HEIGHT:
            # Игра завершается, если пропущена монета
            running = False

    # отрисовка
    pygame.draw.rect(screen, (0, 0, 255), player)
    for coin in coins:
        pygame.draw.ellipse(screen, YELLOW, coin)

    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # отображение рекорда
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(high_score_text, (WIDTH - 200, 10))

    pygame.display.flip()

    # обновляем рекорд, если он побит
    if score > high_score:
        high_score = score
        with open(record_file, "w") as f:
            f.write(str(high_score))

pygame.quit()