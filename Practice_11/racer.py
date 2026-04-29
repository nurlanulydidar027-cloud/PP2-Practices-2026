"""
=====================================================================
  RACER — Practice 11
  Расширение проекта из Practice 8:
    1) Случайная генерация монет с разным "весом" (значение очков)
    2) Скорость врагов растёт, когда игрок собирает N монет
    3) Подробные комментарии в коде
=====================================================================
Управление:
    ← →  — движение машины
    SPACE — рестарт после Game Over
    ESC  — выход
"""

import pygame
import random
import sys
import math

# ---------- Инициализация ----------
pygame.init()

# Размер окна и FPS
WIDTH, HEIGHT = 500, 700
FPS = 60

# Цветовая палитра
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
GRAY       = (50, 50, 50)
ROAD_LINE  = (255, 255, 100)
RED        = (220, 50, 50)
GRASS      = (30, 100, 30)
BRONZE     = (205, 127, 50)
SILVER     = (200, 200, 210)
GOLD       = (255, 215, 0)

# Параметры геймплея
COINS_FOR_BOOST   = 5     # Каждые N монет — буст скорости врагов
SPEED_BOOST_STEP  = 1.2   # Прирост скорости за один буст

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer — Practice 11")
clock = pygame.time.Clock()

# Шрифты
font_small  = pygame.font.SysFont("arial", 18, bold=True)
font_medium = pygame.font.SysFont("arial", 26, bold=True)
font_large  = pygame.font.SysFont("arial", 56, bold=True)


# =====================================================================
#  Класс игрока
# =====================================================================
class Player:
    """Машина игрока. Управление стрелками влево/вправо."""

    def __init__(self):
        self.width, self.height = 50, 80
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 30
        self.speed = 6

    def update(self, keys):
        # Движение в пределах дороги (слева/справа есть трава шириной 50px)
        if keys[pygame.K_LEFT] and self.x > 60:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 60 - self.width:
            self.x += self.speed

    def draw(self, surface):
        # Корпус машины
        pygame.draw.rect(surface, RED,
                         (self.x, self.y, self.width, self.height),
                         border_radius=8)
        # Лобовое стекло
        pygame.draw.rect(surface, (100, 180, 255),
                         (self.x + 8, self.y + 15, self.width - 16, 22),
                         border_radius=4)
        # Заднее стекло
        pygame.draw.rect(surface, (60, 100, 160),
                         (self.x + 8, self.y + self.height - 30,
                          self.width - 16, 18), border_radius=4)
        # Колёса
        for wy in (self.y + 10, self.y + self.height - 28):
            pygame.draw.rect(surface, BLACK, (self.x - 4, wy, 6, 18))
            pygame.draw.rect(surface, BLACK,
                             (self.x + self.width - 2, wy, 6, 18))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


# =====================================================================
#  Класс врага
# =====================================================================
class Enemy:
    """Машина-противник, едет сверху вниз."""

    def __init__(self, speed):
        self.width, self.height = 50, 80
        self.x = random.randint(70, WIDTH - 70 - self.width)
        self.y = -self.height
        self.speed = speed
        # Случайный цвет, чтобы было разнообразие
        self.color = random.choice([
            (50, 100, 220), (200, 100, 200),
            (100, 220, 100), (255, 165, 0), (180, 180, 180)
        ])

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height),
                         border_radius=8)
        # Лобовое стекло (внизу — машина едет на нас)
        pygame.draw.rect(surface, (100, 180, 255),
                         (self.x + 8, self.y + self.height - 38,
                          self.width - 16, 22), border_radius=4)
        for wy in (self.y + 10, self.y + self.height - 28):
            pygame.draw.rect(surface, BLACK, (self.x - 4, wy, 6, 18))
            pygame.draw.rect(surface, BLACK,
                             (self.x + self.width - 2, wy, 6, 18))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        return self.y > HEIGHT


# =====================================================================
#  Класс монеты с весом
# =====================================================================
class Coin:
    """
    Монета с разным весом. Тип выбирается случайно
    с учётом вероятностей: бронза — часто, золото — редко.
    Структура TYPES: (значение_очков, цвет, шанс_появления, радиус)
    """
    TYPES = [
        (1, BRONZE, 60, 12),   # Бронза: значение 1, шанс ~60%
        (3, SILVER, 30, 14),   # Серебро: значение 3, шанс ~30%
        (5, GOLD,   10, 16),   # Золото: значение 5, шанс ~10%
    ]

    def __init__(self, speed):
        # Выбираем тип монеты согласно весам вероятностей
        weights = [t[2] for t in Coin.TYPES]
        coin_type = random.choices(Coin.TYPES, weights=weights, k=1)[0]
        self.value, self.color, _, self.radius = coin_type

        self.x = random.randint(70 + self.radius, WIDTH - 70 - self.radius)
        self.y = -self.radius
        self.speed = speed
        self.angle = 0  # Угол для эффекта вращения

    def update(self):
        self.y += self.speed
        self.angle = (self.angle + 6) % 360  # Анимация поворота

    def draw(self, surface):
        # Эффект вращения: ширина монеты пульсирует через косинус угла
        w = max(2, abs(math.cos(math.radians(self.angle))) * self.radius)
        # Внешний контур (золотая/серебряная/бронзовая)
        pygame.draw.ellipse(
            surface, self.color,
            (self.x - w, self.y - self.radius, w * 2, self.radius * 2))
        # Тёмный край
        pygame.draw.ellipse(
            surface, (60, 40, 0),
            (self.x - w, self.y - self.radius, w * 2, self.radius * 2), 2)
        # Цифра номинала видна, только когда монета достаточно широкая
        if w > 8:
            text = font_small.render(str(self.value), True, BLACK)
            surface.blit(text,
                         (self.x - text.get_width() // 2,
                          self.y - text.get_height() // 2))

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2, self.radius * 2)

    def is_off_screen(self):
        return self.y > HEIGHT


# =====================================================================
#  Дорога с анимацией разметки
# =====================================================================
class Road:
    """Прокручиваемая дорога с пунктирной разметкой посередине."""

    def __init__(self):
        self.line_y = 0

    def update(self, speed):
        # Сдвигаем разметку вниз; используем модуль 60 для зацикливания
        self.line_y = (self.line_y + speed) % 60

    def draw(self, surface):
        # Трава по краям
        pygame.draw.rect(surface, GRASS, (0, 0, 50, HEIGHT))
        pygame.draw.rect(surface, GRASS, (WIDTH - 50, 0, 50, HEIGHT))
        # Асфальт
        pygame.draw.rect(surface, GRAY, (50, 0, WIDTH - 100, HEIGHT))
        # Сплошные белые полосы по краям дороги
        pygame.draw.rect(surface, WHITE, (50, 0, 4, HEIGHT))
        pygame.draw.rect(surface, WHITE, (WIDTH - 54, 0, 4, HEIGHT))
        # Жёлтая пунктирная разметка посередине
        for i in range(-1, HEIGHT // 60 + 2):
            y = i * 60 + self.line_y
            pygame.draw.rect(surface, ROAD_LINE,
                             (WIDTH // 2 - 3, y, 6, 30))


# =====================================================================
#  Экран Game Over
# =====================================================================
def show_game_over(surface, score, coins, boosts):
    """Полупрозрачное затемнение и текст поражения."""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))

    title = font_large.render("GAME OVER", True, RED)
    s1    = font_medium.render(f"Score: {score}", True, WHITE)
    s2    = font_medium.render(f"Coins: {coins}", True, GOLD)
    s3    = font_small.render(f"Speed boosts triggered: {boosts}", True, WHITE)
    s4    = font_small.render("SPACE — restart   ESC — quit", True, WHITE)

    surface.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    surface.blit(s1,    (WIDTH // 2 - s1.get_width()    // 2, HEIGHT // 2))
    surface.blit(s2,    (WIDTH // 2 - s2.get_width()    // 2, HEIGHT // 2 + 36))
    surface.blit(s3,    (WIDTH // 2 - s3.get_width()    // 2, HEIGHT // 2 + 76))
    surface.blit(s4,    (WIDTH // 2 - s4.get_width()    // 2, HEIGHT // 2 + 120))


# =====================================================================
#  Главный игровой цикл
# =====================================================================
def main():
    # Инициализация состояния
    player  = Player()
    road    = Road()
    enemies = []
    coins   = []

    score             = 0
    coins_collected   = 0
    enemy_speed       = 4.0
    coin_speed        = 5.0
    boost_count       = 0   # Сколько раз сработал буст скорости

    enemy_spawn_timer = 0
    coin_spawn_timer  = 0

    game_over = False
    flash_timer = 0  # Краткая вспышка при срабатывании буста

    while True:
        clock.tick(FPS)

        # ---- Обработка событий ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_SPACE and game_over:
                    return main()  # Перезапуск игры

        if not game_over:
            # ---- Логика ----
            keys = pygame.key.get_pressed()
            player.update(keys)

            # Спавн врагов с интервалом
            enemy_spawn_timer += 1
            if enemy_spawn_timer > 80:
                enemies.append(Enemy(enemy_speed))
                enemy_spawn_timer = 0

            # Спавн монет с интервалом
            coin_spawn_timer += 1
            if coin_spawn_timer > 55:
                coins.append(Coin(coin_speed))
                coin_spawn_timer = 0

            # Анимация дороги (скорость зависит от текущей скорости врагов)
            road.update(enemy_speed)

            # Обновление врагов и проверка столкновений
            for enemy in enemies[:]:
                enemy.update()
                if enemy.is_off_screen():
                    enemies.remove(enemy)
                    score += 10  # Очки за уклонение
                elif enemy.get_rect().colliderect(player.get_rect()):
                    game_over = True

            # Обновление монет, проверка сбора и срабатывания буста
            for coin in coins[:]:
                coin.update()
                if coin.is_off_screen():
                    coins.remove(coin)
                elif coin.get_rect().colliderect(player.get_rect()):
                    coins_collected += coin.value
                    score += coin.value * 5
                    coins.remove(coin)

                    # Проверка: достигнут ли новый порог N монет?
                    new_boost = coins_collected // COINS_FOR_BOOST
                    if new_boost > boost_count:
                        boost_count = new_boost
                        enemy_speed += SPEED_BOOST_STEP
                        # Обновляем скорость уже летящих врагов
                        for e in enemies:
                            e.speed = enemy_speed
                        flash_timer = 30  # Вспышка экрана на 0.5 сек

            if flash_timer > 0:
                flash_timer -= 1

        # ---- Отрисовка ----
        screen.fill(BLACK)
        road.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)
        for coin in coins:
            coin.draw(screen)

        player.draw(screen)

        # Полупрозрачная вспышка при бусте
        if flash_timer > 0:
            flash = pygame.Surface((WIDTH, HEIGHT))
            flash.set_alpha(int(flash_timer * 4))
            flash.fill((255, 80, 80))
            screen.blit(flash, (0, 0))

        # ---- HUD ----
        hud = pygame.Surface((WIDTH, 44))
        hud.set_alpha(180)
        hud.fill(BLACK)
        screen.blit(hud, (0, 0))

        screen.blit(font_medium.render(f"Score: {score}", True, WHITE), (10, 8))
        coins_text = font_medium.render(f"Coins: {coins_collected}", True, GOLD)
        screen.blit(coins_text, (WIDTH - coins_text.get_width() - 10, 8))
        speed_text = font_small.render(
            f"Enemy speed: {enemy_speed:.1f}  (boost x{boost_count})",
            True, WHITE)
        screen.blit(speed_text,
                    (WIDTH // 2 - speed_text.get_width() // 2, 14))

        if game_over:
            show_game_over(screen, score, coins_collected, boost_count)

        pygame.display.flip()


if __name__ == "__main__":
    main()