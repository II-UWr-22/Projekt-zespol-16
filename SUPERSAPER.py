import pygame
import random
import sys
pygame.init()
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Super Saper")
background_colour = (200,200,200)
screen.fill(background_colour)
game_over = False
class state:
    def init(self):
        self.board_size = (10, 10)
        self.mines = (self.board_size[0]-1)*(self.board_size[1]-1)
        self.board = [[None for _ in range(self.board_size[0])] for _ in range(self.board_size[1])]
while not game_over:
    pygame.display.flip()
    font = pygame.font.SysFont(None, 72)
    img = font.render('       SUPER SAPER', True, 'Dark Green')
    screen.blit(img, (20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True