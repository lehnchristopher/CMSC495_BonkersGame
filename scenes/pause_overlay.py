import pygame
import os
from common import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, YELLOW, ROOT_PATH

# --- Pause Sounds ---
try:
    pause_sound = pygame.mixer.Sound(os.path.join(ROOT_PATH, "media", "audio", "pause.mp3"))
except:
    pause_sound = None

try:
    unpause_sound = pygame.mixer.Sound(os.path.join(ROOT_PATH, "media", "audio", "unpause.mp3"))
except:
    unpause_sound = None


def pause_overlay(snapshot):
    """Pause screen"""
    screen = pygame.display.get_surface()

    # Font setup
    font_path = os.path.join(ROOT_PATH, 'media', 'graphics', 'font', 'Pixeboy.ttf')
    font_big = pygame.font.Font(font_path, 120)
    font_small = pygame.font.Font(font_path, 48)

    clock = pygame.time.Clock()

    # Frozen frame
    screen.blit(snapshot, (0, 0))

    # Play pause sound
    if pause_sound:
        pause_sound.play()

    while True:
        # Text
        title = font_big.render("PAUSED", True, YELLOW)
        quit_text = font_small.render("Press Q to Quit", True, WHITE)
        or_text = font_small.render("or", True, WHITE)
        resume_text = font_small.render("Press Space Bar to Resume", True, WHITE)

        # Center text block
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 150))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(or_text, (SCREEN_WIDTH // 2 - or_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2 + 70))

        # Input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "menu"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if unpause_sound:
                        unpause_sound.play()
                    return "resume"
                if event.key == pygame.K_q:
                    return "menu"

        pygame.display.flip()
        clock.tick(60)
