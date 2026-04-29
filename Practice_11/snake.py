"""
=====================================================================
  SNAKE — Practice 11
  Расширение проекта из Practice 8:
    1) Случайная генерация еды с разным "весом" (значение очков)
    2) Еда, которая исчезает по таймеру
    3) Подробные комментарии в коде
=====================================================================
Управление:
    ← ↑ → ↓  или  WASD  — движение змейки
    SPACE                — рестарт после Game Over
    ESC                  — выход
"""

import pygame
import random
import sys
import math

pygame.init()

# ---------- Параметры поля ----------
CELL_SIZE = 25
GRID_W, GRID_H = 24, 22
HUD_HEIGHT = 70
WIDTH  = CELL_SIZE * GRID_W
HEIGHT = CELL_SIZE * GRID_H + HUD_HEIGHT
SNAKE_FPS = 12  # Скорость змейки (ходов в секунду)

# ---------- Палитра ----------
BG_DARK    = (15, 25, 35)
BG_LIGHT   = (20, 30, 40)
SNAKE_HEAD = (110, 240, 130)
WHITE      = (240, 240, 240)
RED        = (220, 60, 60)
GOLD       = (255, 200, 50)
PURPLE     = (180, 80, 220)
TIMER_RED  = (255, 100, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake — Practice 11")
clock = pygame.time.Clock()

font_small  = pygame.font.SysFont("arial", 16, bold=True)
font_medium = pygame.font.SysFont("arial", 22, bold=True)
font_large  = pygame.font.SysFont("arial", 50, bold=True)


# =====================================================================
#  Класс змейки
# =====================================================================
class Snake:
    """Змейка: список координат сегментов в клетках поля."""

    def __init__(self):
        # Стартует в центре поля, направляется вправо
        cx, cy = GRID_W // 2, GRID_H // 2
        self.body = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.grow = 0  # Сколько ещё сегментов добавить

    def change_direction(self, new_dir):
        # Запрет разворота на 180° (нельзя въехать в самого себя)
        if (new_dir[0] != -self.direction[0] or
                new_dir[1] != -self.direction[1]):
            self.next_direction = new_dir

    def update(self):
        """Один шаг змейки."""
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0],
                    head_y + self.direction[1])
        self.body.insert(0, new_head)
        # Хвост убираем, только если не растём
        if self.grow > 0:
            self.grow -= 1
        else:
            self.body.pop()

    def head(self):
        return self.body[0]

    def check_collision(self):
        """Проверка столкновения со стеной или собой."""
        hx, hy = self.body[0]
        if hx < 0 or hx >= GRID_W or hy < 0 or hy >= GRID_H:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    def draw(self, surface):
        for i, (x, y) in enumerate(self.body):
            px = x * CELL_SIZE
            py = y * CELL_SIZE + HUD_HEIGHT
            if i == 0:
                # Голова
                pygame.draw.rect(surface, SNAKE_HEAD,
                                 (px + 1, py + 1,
                                  CELL_SIZE - 2, CELL_SIZE - 2),
                                 border_radius=6)
                # Глаза смотрят в направлении движения
                eo = 6  # eye offset
                if self.direction == (1, 0):
                    e1, e2 = (px + CELL_SIZE - eo, py + 7), \
                             (px + CELL_SIZE - eo, py + CELL_SIZE - 7)
                elif self.direction == (-1, 0):
                    e1, e2 = (px + eo, py + 7), \
                             (px + eo, py + CELL_SIZE - 7)
                elif self.direction == (0, -1):
                    e1, e2 = (px + 7, py + eo), \
                             (px + CELL_SIZE - 7, py + eo)
                else:
                    e1, e2 = (px + 7, py + CELL_SIZE - eo), \
                             (px + CELL_SIZE - 7, py + CELL_SIZE - eo)
                pygame.draw.circle(surface, BG_DARK, e1, 3)
                pygame.draw.circle(surface, BG_DARK, e2, 3)
            else:
                # Тело: цвет слегка темнеет к хвосту (градиент)
                shade = max(80, 200 - i * 4)
                color = (40, shade, 70)
                pygame.draw.rect(surface, color,
                                 (px + 2, py + 2,
                                  CELL_SIZE - 4, CELL_SIZE - 4),
                                 border_radius=5)


# =====================================================================
#  Класс еды с весом и таймером
# =====================================================================
class Food:
    """
    Еда с разным "весом" (значением). Тип выбирается случайно
    с учётом вероятностей. У ценной еды есть таймер исчезновения.
    Структура TYPES:
      (label, очки, цвет, шанс_появления, таймер_сек или None)
    """
    TYPES = [
        ("normal", 1, RED,    70, None),  # Обычная: вечная, дёшево
        ("golden", 3, GOLD,   22,    8),  # Золотая: 3 очка, 8 секунд
        ("magic",  5, PURPLE,  8,    4),  # Магическая: 5 очков, 4 секунды
    ]

    def __init__(self, occupied):
        # Выбор типа еды по весам вероятностей
        weights = [t[3] for t in Food.TYPES]
        ftype = random.choices(Food.TYPES, weights=weights, k=1)[0]
        self.label, self.points, self.color, _, self.timer_max = ftype
        self.timer = self.timer_max  # Оставшееся время в секундах

        # Размещаем в случайной свободной клетке
        for _ in range(200):
            self.x = random.randint(0, GRID_W - 1)
            self.y = random.randint(0, GRID_H - 1)
            if (self.x, self.y) not in occupied:
                return
        # Если поле почти заполнено — берём что есть
        self.x = random.randint(0, GRID_W - 1)
        self.y = random.randint(0, GRID_H - 1)

    def update(self, dt):
        """Уменьшаем таймер на dt секунд (если он есть)."""
        if self.timer is not None:
            self.timer -= dt

    def expired(self):
        return self.timer is not None and self.timer <= 0

    def position(self):
        return (self.x, self.y)

    def draw(self, surface):
        px = self.x * CELL_SIZE
        py = self.y * CELL_SIZE + HUD_HEIGHT
        cx, cy = px + CELL_SIZE // 2, py + CELL_SIZE // 2

        # Пульсация для еды с таймером
        if self.timer_max is not None:
            pulse = abs((pygame.time.get_ticks() // 80) % 10 - 5) / 5
            radius = int(CELL_SIZE / 2 - 2 - pulse * 2)
        else:
            radius = CELL_SIZE // 2 - 2

        # Сама еда
        pygame.draw.circle(surface, self.color, (cx, cy), radius)
        # Блик
        pygame.draw.circle(surface, WHITE, (cx - 3, cy - 3), 3)

        # Кольцо-индикатор остатка времени
        if self.timer_max is not None and self.timer is not None:
            ratio = max(0, self.timer / self.timer_max)
            ring_rect = pygame.Rect(px + 1, py + 1,
                                    CELL_SIZE - 2, CELL_SIZE - 2)
            try:
                pygame.draw.arc(surface, WHITE, ring_rect,
                                -math.pi / 2,
                                -math.pi / 2 + 2 * math.pi * ratio, 2)
            except Exception:
                pass


# =====================================================================
#  Отрисовка фона и HUD
# =====================================================================
def draw_grid(surface):
    """Шахматный фон поля."""
    for y in range(GRID_H):
        for x in range(GRID_W):
            color = BG_DARK if (x + y) % 2 == 0 else BG_LIGHT
            pygame.draw.rect(surface, color,
                             (x * CELL_SIZE,
                              y * CELL_SIZE + HUD_HEIGHT,
                              CELL_SIZE, CELL_SIZE))


def draw_hud(surface, score):
    """Верхняя информационная панель."""
    pygame.draw.rect(surface, (10, 15, 20), (0, 0, WIDTH, HUD_HEIGHT))
    pygame.draw.rect(surface, (40, 60, 80),
                     (0, HUD_HEIGHT - 2, WIDTH, 2))

    # Очки слева
    surface.blit(font_medium.render(f"Score: {score}", True, WHITE),
                 (15, 22))

    # Легенда справа: значение каждого типа еды
    legend_x = WIDTH - 305
    surface.blit(font_small.render("Food types:", True, WHITE),
                 (legend_x, 6))
    for i, (label, pts, color, _, t) in enumerate(Food.TYPES):
        x = legend_x + i * 100
        y = 26
        pygame.draw.circle(surface, color, (x + 10, y + 10), 7)
        surface.blit(font_small.render(f"+{pts}", True, WHITE),
                     (x + 22, y))
        if t:
            surface.blit(font_small.render(f"{t}s", True, TIMER_RED),
                         (x + 22, y + 14))
        else:
            surface.blit(font_small.render("∞", True, (180, 180, 180)),
                         (x + 22, y + 14))


def show_game_over(surface, score):
    """Полупрозрачное окно с финальным счётом."""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    surface.blit(overlay, (0, 0))

    title = font_large.render("GAME OVER", True, RED)
    s1 = font_medium.render(f"Final Score: {score}", True, WHITE)
    s2 = font_small.render("SPACE — restart   ESC — quit", True, WHITE)

    surface.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    surface.blit(s1,    (WIDTH // 2 - s1.get_width()    // 2, HEIGHT // 2))
    surface.blit(s2,    (WIDTH // 2 - s2.get_width()    // 2, HEIGHT // 2 + 50))


# =====================================================================
#  Главный цикл
# =====================================================================
def main():
    snake = Snake()
    foods = [Food(set(snake.body))]  # На поле всегда есть как минимум 1 еда
    score = 0

    EXTRA_FOOD_INTERVAL = 3.0  # Раз в 3 сек пробуем добавить ещё еды
    MAX_FOODS = 4
    extra_food_timer = 0.0

    # Шаги змейки делаем по таймеру, а рендер на 60 FPS
    move_interval = 1.0 / SNAKE_FPS
    move_timer    = 0.0

    last_time = pygame.time.get_ticks() / 1000.0
    game_over = False

    while True:
        clock.tick(60)
        now = pygame.time.get_ticks() / 1000.0
        dt = now - last_time
        last_time = now

        # ---- События ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if event.key == pygame.K_SPACE and game_over:
                    return main()  # Перезапуск
                if not game_over:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        snake.change_direction((0, -1))
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        snake.change_direction((0, 1))
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        snake.change_direction((-1, 0))
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        snake.change_direction((1, 0))

        if not game_over:
            # ---- Обновление еды (таймеры) ----
            for food in foods[:]:
                food.update(dt)
                if food.expired():
                    foods.remove(food)

            # На поле всегда должна быть хотя бы одна обычная еда
            if not foods:
                foods.append(Food(set(snake.body)))

            # Время от времени добавляем дополнительную еду
            extra_food_timer += dt
            if extra_food_timer >= EXTRA_FOOD_INTERVAL and len(foods) < MAX_FOODS:
                extra_food_timer = 0
                occupied = set(snake.body) | {f.position() for f in foods}
                foods.append(Food(occupied))

            # ---- Шаг змейки ----
            move_timer += dt
            if move_timer >= move_interval:
                move_timer = 0
                snake.update()

                # Поедание еды
                for food in foods[:]:
                    if snake.head() == food.position():
                        score += food.points
                        # Чем ценнее еда, тем больше прирост в длину
                        snake.grow += food.points
                        foods.remove(food)

                if snake.check_collision():
                    game_over = True

        # ---- Отрисовка ----
        screen.fill(BG_DARK)
        draw_grid(screen)
        for food in foods:
            food.draw(screen)
        snake.draw(screen)
        draw_hud(screen, score)

        if game_over:
            show_game_over(screen, score)

        pygame.display.flip()


if __name__ == "__main__":
    main()