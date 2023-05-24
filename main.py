import pygame
import numpy as np

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('N Queen Puzzle')

# Global Variables
clicked = False

light = {}
dark = {}

player = 1

board = np.empty((8,8), dtype=object)

states = []
# actions are 'piece': [((x,y)), canMulti, swappable, initMove]
actions = { 
    'pa': [((-1,0)), False, False, (0,2)],
    'ro': [((1,0)), True, True, None],
    'kn': [((2,1)), False, True, None],
    'bi': [((1,1)), False, True, None],
    'qu': [((1,1), (1,0)), True, True, None],
    'qu': [((1,1), (1,0)), False, True, None]
}

def init_state():
    for i in range(8):
        dark[f'd_pa_{i}'] = np.array((i, 1))
        light[f'l_pa_{i}'] = np.array((i, 6))
        
    light['l_ro_1'] = np.array((0, 7))
    light['l_kn_1'] = np.array((1, 7))
    light['l_bi_1'] = np.array((2, 7))
    light['l_qu_1'] = np.array((3, 7))
    light['l_ki_2'] = np.array((4, 7))
    light['l_bi_2'] = np.array((5, 7))
    light['l_kn_2'] = np.array((6, 7))
    light['l_ro_2'] = np.array((7, 7))

    dark['d_ro_1'] = np.array((0, 0))
    dark['d_kn_1'] = np.array((1, 0))
    dark['d_bi_1'] = np.array((2, 0))
    dark['d_qu_1'] = np.array((3, 0))
    dark['d_ki_2'] = np.array((4, 0))
    dark['d_bi_2'] = np.array((5, 0))
    dark['d_kn_2'] = np.array((6, 0))
    dark['d_ro_2'] = np.array((7, 0))

    state = []

    states.append((light, dark))

def init_board():
    c = 1
    checkers = {-1: (163, 82, 78), 1: (242, 232, 231)}
    for i in range(8):
        for j in range(8):
            c *= -1
            board[i,j] = ((checkers[c], pygame.Rect(j*100, i*100, 100, 100)))
        c *= -1    

def draw_board():
    for i in range(8):
        for j in range(8):
            screen.fill(*board[i,j])

def draw_state():
    state = states[-1]
    # Draw light pieces
    for l, v in state[0].items():
        img = pygame.image.load(f'./assets/{l[:4]}.png')
        screen.blit(img, v*100 + (20,15))

    for d, v in state[1].items():
        img = pygame.image.load(f'./assets/{d[:4]}.png')
        screen.blit(img, v*100 + (20,15))

init_board()
init_state()

run = True
while run:
    draw_board()
    draw_state()

    # Event Handlers
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
        if (event.type == pygame.MOUSEBUTTONDOWN and clicked == False):
            clicked == True
        if (event.type == pygame.MOUSEBUTTONUP and clicked == True):
            clicked = False
            pos = pygame.mouse.get_pos()
            pos_x = pos[0]
            pos_y = pos[1]
        pass

    pygame.display.update()