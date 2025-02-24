import pygame

def init_game_over_text(screen_width, screen_height):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    return text, text_rect

def show_game_over(screen, text, text_rect):
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    