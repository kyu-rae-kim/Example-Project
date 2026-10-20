"""Snake 실행 파일: python main.py"""
import sys

import pygame

from settings import *
from snake import Snake, UP, DOWN, LEFT, RIGHT

KEYS = {
    pygame.K_UP: UP, pygame.K_w: UP,
    pygame.K_DOWN: DOWN, pygame.K_s: DOWN,
    pygame.K_LEFT: LEFT, pygame.K_a: LEFT,
    pygame.K_RIGHT: RIGHT, pygame.K_d: RIGHT,
}


def draw_cell(screen, pos, color):
    rect = pygame.Rect(pos[0] * CELL, pos[1] * CELL, CELL, CELL)
    pygame.draw.rect(screen, color, rect.inflate(-2, -2), border_radius=5)


def draw(screen, font, big, game, best, paused):
    screen.fill(BG)
    for x in range(COLS):
        for y in range(ROWS):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, GRID, (x * CELL, y * CELL, CELL, CELL))
    for obs in game.obstacles:
        draw_cell(screen, obs, OBSTACLE)
    if game.food:
        draw_cell(screen, game.food, FOOD)
    for i, seg in enumerate(game.body):
        draw_cell(screen, seg, SNAKE_HEAD if i == 0 else SNAKE_BODY)

    pygame.draw.rect(screen, PANEL, (0, ROWS * CELL, WIDTH, 40))
    info = font.render(f"Score {game.score}   Best {best}", True, TEXT)
    screen.blit(info, (12, ROWS * CELL + 10))

    msg = None
    if not game.alive:
        msg = "Game Over - SPACE: restart"
    elif paused:
        msg = "Paused - P: resume"
    if msg:
        text = big.render(msg, True, TEXT)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, ROWS * CELL // 2)))


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 26)
    big = pygame.font.SysFont(None, 40)

    game = Snake()
    best = 0
    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in KEYS and not paused:
                    game.turn(KEYS[event.key])
                elif event.key == pygame.K_p and game.alive:
                    paused = not paused
                elif event.key == pygame.K_SPACE and not game.alive:
                    game.reset()

        if not paused:
            game.step()
        best = max(best, game.score)
        draw(screen, font, big, game, best, paused)
        pygame.display.flip()
        # 점수가 오를수록 빨라진다
        clock.tick(min(FPS_START + game.score // 30, FPS_MAX))


if __name__ == "__main__":
    main()
