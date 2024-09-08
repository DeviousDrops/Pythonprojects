import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 16, 16
MINE_COUNT = 40
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (169, 169, 169)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)
END_FONT = pygame.font.Font(None, 72)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minesweeper')

# Load images
flag_img = pygame.transform.scale(pygame.image.load("D:/downloads/flag.png"), (TILE_SIZE, TILE_SIZE))
mine_img = pygame.transform.scale(pygame.image.load("D:/downloads/mine.png"), (TILE_SIZE, TILE_SIZE))
title_img = pygame.transform.scale(pygame.image.load("D:/downloads/display.png"), (WIDTH, HEIGHT))

# Board and minefield setup
def create_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < mines:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if (x, y) not in mine_positions:
            mine_positions.add((x, y))
            board[x][y] = -1  # -1 represents a mine

    # Update the board with numbers
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == -1:
                continue
            count = sum((board[i][j] == -1) for i in range(max(0, x-1), min(rows, x+2)) for j in range(max(0, y-1), min(cols, y+2)))
            board[x][y] = count

    return board, mine_positions

# Draw the board
def draw_board(screen, board, revealed, flagged):
    for x in range(ROWS):
        for y in range(COLS):
            rect = pygame.Rect(y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if revealed[x][y]:
                pygame.draw.rect(screen, DARK_GRAY, rect)
                if board[x][y] == -1:
                    screen.blit(mine_img, rect.topleft)
                elif board[x][y] > 0:
                    text = FONT.render(str(board[x][y]), True, BLACK)
                    screen.blit(text, (y * TILE_SIZE + TILE_SIZE // 3, x * TILE_SIZE + TILE_SIZE // 6))
            else:
                pygame.draw.rect(screen, GRAY, rect)
                if (x, y) in flagged:
                    screen.blit(flag_img, rect.topleft)
            pygame.draw.rect(screen, BLACK, rect, 2)

# Reveal cells
def reveal(board, revealed, x, y):
    if revealed[x][y]:
        return

    revealed[x][y] = True

    if board[x][y] == 0:
        for i in range(max(0, x-1), min(ROWS, x+2)):
            for j in range(max(0, y-1), min(COLS, y+2)):
                if not revealed[i][j]:
                    reveal(board, revealed, i, j)

# Show the title screen
def show_title_screen(screen):
    screen.blit(title_img, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)

# Show the end game message
def show_end_screen(screen):
    screen.fill(WHITE)
    end_text = END_FONT.render("ALLAH HU AKBAR", True, RED)
    text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(end_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

# Main game loop
def main():
    show_title_screen(screen)
    
    board, mine_positions = create_board(ROWS, COLS, MINE_COUNT)
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    flagged = set()
    game_over = False

    while True:
        screen.fill(WHITE)
        draw_board(screen, board, revealed, flagged)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos[1] // TILE_SIZE, event.pos[0] // TILE_SIZE
                if event.button == 1:  # Left click
                    if (x, y) in flagged:
                        continue
                    if board[x][y] == -1:
                        revealed[x][y] = True
                        game_over = True
                        draw_board(screen, board, revealed, flagged)
                        pygame.display.flip()
                        show_end_screen(screen)
                        pygame.quit()
                        sys.exit()
                    else:
                        reveal(board, revealed, x, y)
                elif event.button == 3:  # Right click
                    if (x, y) not in revealed:
                        if (x, y) in flagged:
                            flagged.remove((x, y))
                        else:
                            flagged.add((x, y))

        pygame.display.flip()

if __name__ == "__main__":
    main()
