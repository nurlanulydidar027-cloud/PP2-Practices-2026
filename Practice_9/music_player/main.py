import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# Настройки окна
WIDTH, HEIGHT = 500, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Цвета
BG_COLOR = (30, 30, 50)
WHITE = (255, 255, 255)
GREEN = (80, 200, 100)
RED = (200, 80, 80)
GRAY = (150, 150, 150)
YELLOW = (255, 220, 80)
CYAN = (80, 200, 220)

# Шрифты
title_font = pygame.font.SysFont("Arial", 32, bold=True)
font = pygame.font.SysFont("Arial", 22)
small_font = pygame.font.SysFont("Arial", 16)

# Загрузка треков из папки music/
MUSIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "music")

# Если папки нет — создаём
if not os.path.exists(MUSIC_DIR):
    os.makedirs(MUSIC_DIR)

# Собираем все аудио файлы
playlist = []
for f in sorted(os.listdir(MUSIC_DIR)):
    if f.lower().endswith(('.mp3', '.wav', '.ogg')):
        playlist.append(f)

current_track = 0
is_playing = False
status_message = "Press P to play"


def play_track():
    """Воспроизвести текущий трек"""
    global is_playing, status_message
    if not playlist:
        status_message = "No tracks in music/ folder!"
        return
    try:
        filepath = os.path.join(MUSIC_DIR, playlist[current_track])
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        is_playing = True
        status_message = "Playing"
    except Exception as e:
        status_message = f"Error: {e}"


def stop_track():
    """Остановить воспроизведение"""
    global is_playing, status_message
    pygame.mixer.music.stop()
    is_playing = False
    status_message = "Stopped"


def next_track():
    """Следующий трек"""
    global current_track
    if playlist:
        current_track = (current_track + 1) % len(playlist)
        play_track()


def prev_track():
    """Предыдущий трек"""
    global current_track
    if playlist:
        current_track = (current_track - 1) % len(playlist)
        play_track()


def draw_ui():
    """Рисуем интерфейс плеера"""
    screen.fill(BG_COLOR)

    # Заголовок
    title = title_font.render("Music Player", True, CYAN)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    # Текущий трек
    if playlist:
        track_name = playlist[current_track]
        # Обрезаем длинные названия
        if len(track_name) > 40:
            track_name = track_name[:37] + "..."
        track_text = font.render(track_name, True, WHITE)
        track_num = small_font.render(f"Track {current_track + 1} / {len(playlist)}", True, GRAY)
    else:
        track_text = font.render("No tracks found", True, RED)
        track_num = small_font.render("Add .mp3/.wav/.ogg to music/ folder", True, GRAY)

    screen.blit(track_text, (WIDTH // 2 - track_text.get_width() // 2, 90))
    screen.blit(track_num, (WIDTH // 2 - track_num.get_width() // 2, 120))

    # Статус
    color = GREEN if is_playing else RED
    status = font.render(status_message, True, color)
    screen.blit(status, (WIDTH // 2 - status.get_width() // 2, 165))

    # Управление
    controls = [
        ("[P] Play", GREEN),
        ("[S] Stop", RED),
        ("[N] Next", YELLOW),
        ("[B] Back", YELLOW),
        ("[Q] Quit", GRAY),
    ]

    y = 230
    for text, color in controls:
        label = font.render(text, True, color)
        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, y))
        y += 28

    pygame.display.flip()


# Главный цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_track()
            elif event.key == pygame.K_s:
                stop_track()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_q:
                running = False

    # Проверяем, закончился ли трек — автоматически следующий
    if is_playing and not pygame.mixer.music.get_busy():
        next_track()

    draw_ui()
    clock.tick(30)

pygame.mixer.music.stop()
pygame.quit()
sys.exit()