#############################    IMPORTATIONS    ############################

import pygame, os, math
from pygame.locals import *


#############################    FONCTIONS    ############################

def levels(la_difficulte):

    #############################    VARIABLES    ############################

    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    ##### 4 X 4 #####
    lvl1_4x4 = [0, 0, 2, 0], [0.5, 0, 0, 0], [0, 20, 1.5, 2], [0, 0, 10, 0]
    sol_lvl1_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl2_4x4 = [0, 0, 4, 0], [1, 0, 40, 0], [0, 40, 3, 4], [0, 0, 10, 0]
    sol_lvl2_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl3_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl3_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl4_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl4_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl5_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl5_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl6_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl6_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl7_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl7_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl8_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl8_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl9_4x4 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl9_4x4 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]

    ##### 5 X 5 #####
    lvl1_5x5 = [2, 3, 0.5, 1, 0], [0, 0, 0, 0, 30], [0, 0, 0.5, 0 , 0], [0, 0, 1, 2, 1], [0, 0, 0, 0, 0]
    sol_lvl1_5x5 = [[5, 2, 3, 4, 1], [4, 1, 2, 5, 3], [3, 4, 1, 2, 5], [1, 5, 4, 3, 2], [2, 3, 5, 1, 4]]
    lvl2_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl2_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl3_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl3_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl4_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl4_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl5_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl5_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl6_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl6_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl7_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl7_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl8_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl8_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    lvl9_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    sol_lvl9_5x5 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]

    ##### 6 X 6 #####
    lvl1_6x6 = [0, 0, 4, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0], [0, 0, 10, 0, 0, 0]
    sol_lvl1_6x6 = [[0, 0, 4, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0], [0, 0, 10, 0, 0, 0]]
    lvl2_6x6 = [0, 0, 4, 0], [1, 0, 40, 0], [0, 40, 3, 4], [0, 0, 10, 0]
    sol_lvl2_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl3_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl3_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl4_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl4_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl5_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl5_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl6_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl6_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl7_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl7_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl8_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl8_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl9_6x6 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl9_6x6 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]

    ##### 7 X 7 #####
    lvl1_7x7 = [0, 0, 4, 0, 0, 10, 0], [1, 0, 0, 0, 0, 10, 0], [0, 20, 3, 4, 0, 10, 0], [0, 0, 10, 0, 0, 10, 0],\
               [1, 0, 0, 0, 0, 10, 0], [0, 20, 3, 4, 0, 10, 0], [0, 0, 10, 0, 0, 10, 0]
    sol_lvl1_7x7 = [0, 0, 4, 0, 0, 10, 0], [1, 0, 0, 0, 0, 10, 0], [0, 20, 3, 4, 0, 10, 0], [0, 0, 10, 0, 0, 10, 0],\
               [1, 0, 0, 0, 0, 10, 0], [0, 20, 3, 4, 0, 10, 0], [0, 0, 10, 0, 0, 10, 0]
    lvl2_7x7 = [0, 0, 4, 0], [1, 0, 40, 0], [0, 40, 3, 4], [0, 0, 10, 0]
    sol_lvl2_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl3_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl3_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl4_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl4_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl5_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl5_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl6_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl6_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl7_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl7_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl8_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl8_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]
    lvl9_7x7 = [0, 0, 4, 0], [1, 0, 0, 0], [0, 20, 3, 4], [0, 0, 10, 0]
    sol_lvl9_7x7 = [[2, 1, 3, 4], [3, 4, 2, 1], [1, 2, 4, 3], [4, 3, 1, 2]]

    ##### 8 X 8 #####
    lvl1_8x8 = [0, 0, 4, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], \
               [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], \
               [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0]
    sol_lvl1_8x8 = [0, 0, 4, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], \
               [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0], \
               [0, 20, 3, 4, 0, 0, 0, 0], [0, 20, 3, 4, 0, 0, 0, 0]
    lvl2_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl2_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl3_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl3_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl4_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl4_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl5_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl5_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl6_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl6_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl7_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl7_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl8_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl8_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    lvl9_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl9_8x8 = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]

    ##### 9 X 9 #####
    lvl1_9x9 = [3, 0.5, 0, 0.5, 1, 70, 20, 60, 0], [0, 0, 0, 0, 0, 3.5, 0, 0, 0], [0, 0.5, 31.5, 4, 0, 0.5, 0, 0, 0], \
               [0, 2, 70, 80, 0.5, 40, 60.5, 0, 0], [0, 0, 90, 1.5, 1.5, 0, 40, 71.5, 0], [0, 0, 1.5, 0, 0, 60, 0, 0, 0], \
               [0, 0, 0, 1, 0, 0, 0, 0.5, 0], [0, 0.5, 0, 0, 2, 1, 30, 0.5, 0], [0.5, 0, 20, 50, 0, 0.5, 71.5, 1.5, 0]
    sol_lvl1_9x9 = [[4, 5, 8, 1, 3, 7, 2, 6, 9], [3, 6, 4, 9, 7, 5, 1, 8, 2], [7, 1, 3, 2, 4, 8, 9, 5, 6], \
                   [1, 3, 7, 8, 2, 4, 6, 9, 5], [8, 2, 9, 6, 5, 1, 4, 7, 3], [9, 7, 5, 3, 1, 6, 8, 2, 4], \
                   [2, 8, 1, 4, 6, 9, 5, 3, 7], [5, 4, 6, 7, 9, 2, 3, 1, 8], [6, 9, 2, 5, 8, 3, 7, 4, 1]]
    lvl2_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl2_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl3_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl3_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl4_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl4_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl5_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl5_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl6_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl6_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl7_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl7_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl8_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl8_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    lvl9_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sol_lvl9_9x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]


    Icone = pygame.image.load("assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    running = True  # Vérifie si la fenetre doit rester ouverte
    screen.fill((0, 105, 102))  # met le fond en vert
    difficulte = la_difficulte


    retour = pygame.image.load("assets/retour.png").convert_alpha()
    clickable_area_retour = pygame.Rect((-10, 670), (240, 50))

    G1 = pygame.image.load("assets/G1.png").convert_alpha()  # Lecture des images des niveaux
    G2 = pygame.image.load("assets/G2.png").convert_alpha()
    G3 = pygame.image.load("assets/G3.png").convert_alpha()
    G4 = pygame.image.load("assets/G4.png").convert_alpha()
    G5 = pygame.image.load("assets/G5.png").convert_alpha()
    G6 = pygame.image.load("assets/G6.png").convert_alpha()
    G7 = pygame.image.load("assets/G7.png").convert_alpha()
    G8 = pygame.image.load("assets/G8.png").convert_alpha()
    G9 = pygame.image.load("assets/G9.png").convert_alpha()

    clickable_area_G1 = pygame.Rect((0, 650), (240, 50))

    niveaux_4x4 = pygame.image.load("assets/niveaux_4x4.png").convert_alpha()
    niveaux_5x5 = pygame.image.load("assets/niveaux_5x5.png").convert_alpha()
    niveaux_6x6 = pygame.image.load("assets/niveaux_6x6.png").convert_alpha()
    niveaux_7x7 = pygame.image.load("assets/niveaux_7x7.png").convert_alpha()
    niveaux_8x8 = pygame.image.load("assets/niveaux_8x8.png").convert_alpha()
    niveaux_9x9 = pygame.image.load("assets/niveaux_9x9.png").convert_alpha()


    pygame.draw.rect(screen, (0, 175, 170), (262, 190, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (490, 190, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (717, 190, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (262, 335, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (490, 335, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (717, 335, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (262, 480, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (490, 480, 100, 100))
    pygame.draw.rect(screen, (0, 175, 170), (717, 480, 100, 100))

    clickable_area_G1 = pygame.Rect((262, 190), (100, 100))
    clickable_area_G2 = pygame.Rect((490, 190), (100, 100))
    clickable_area_G3 = pygame.Rect((717, 190), (100, 100))
    clickable_area_G4 = pygame.Rect((262, 335), (100, 100))
    clickable_area_G5 = pygame.Rect((490, 335), (100, 100))
    clickable_area_G6 = pygame.Rect((717, 335), (100, 100))
    clickable_area_G7 = pygame.Rect((262, 480), (100, 100))
    clickable_area_G8 = pygame.Rect((490, 480), (100, 100))
    clickable_area_G9 = pygame.Rect((717, 480), (100, 100))

    if (difficulte == 4):
        screen.blit(niveaux_4x4, (176, 25))
    if (difficulte == 5):
        screen.blit(niveaux_5x5, (176, 25))
    if (difficulte == 6):
        screen.blit(niveaux_6x6, (176, 25))
    if (difficulte == 7):
        screen.blit(niveaux_7x7, (176, 25))
    if (difficulte == 8):
        screen.blit(niveaux_8x8, (176, 25))
    if (difficulte == 9):
        screen.blit(niveaux_9x9, (176, 25))
    screen.blit(G1, (262, 190))  # Affichage des boutons
    screen.blit(G2, (490, 190))
    screen.blit(G3, (717, 190))
    screen.blit(G4, (262, 335))
    screen.blit(G5, (490, 335))
    screen.blit(G6, (717, 335))
    screen.blit(G7, (262, 480))
    screen.blit(G8, (490, 480))
    screen.blit(G9, (717, 480))
    screen.blit(retour, (-10, 670))


    while running:  # Tant que la fentetre est en cours

        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                running = False


            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_retour.collidepoint(event.pos):
                    from interface import definterface
                    definterface()
                if clickable_area_G1.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_4x4, sol_lvl1_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_5x5, sol_lvl1_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_6x6, sol_lvl1_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_7x7, sol_lvl1_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_8x8, sol_lvl1_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl1_9x9, sol_lvl1_9x9)

                if clickable_area_G2.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_4x4, sol_lvl2_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_5x5, sol_lvl2_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_6x6, sol_lvl2_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_7x7, sol_lvl2_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_8x8, sol_lvl2_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl2_9x9, sol_lvl2_9x9)

                if clickable_area_G3.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_4x4, sol_lvl3_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_5x5, sol_lvl3_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_6x6, sol_lvl3_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_7x7, sol_lvl3_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_8x8, sol_lvl3_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl3_9x9, sol_lvl3_9x9)

                if clickable_area_G4.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_4x4, sol_lvl4_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_5x5, sol_lvl4_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_6x6, sol_lvl4_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_7x7, sol_lvl4_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_8x8, sol_lvl4_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl4_9x9, sol_lvl4_9x9)

                if clickable_area_G5.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_4x4, sol_lvl6_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_5x5, sol_lvl6_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_6x6, sol_lvl6_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_7x7, sol_lvl6_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_8x8, sol_lvl6_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl5_9x9, sol_lvl6_9x9)

                if clickable_area_G6.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_4x4, sol_lvl7_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_5x5, sol_lvl7_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_6x6, sol_lvl7_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_7x7, sol_lvl7_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_8x8, sol_lvl7_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl6_9x9, sol_lvl7_9x9)

                if clickable_area_G7.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_4x4, sol_lvl7_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_5x5, sol_lvl7_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_6x6, sol_lvl7_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_7x7, sol_lvl7_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_8x8, sol_lvl7_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl7_9x9, sol_lvl7_9x9)

                if clickable_area_G8.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_4x4, sol_lvl8_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_5x5, sol_lvl8_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_6x6, sol_lvl8_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_7x7, sol_lvl8_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_8x8, sol_lvl8_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl8_9x9, sol_lvl8_9x9)

                if clickable_area_G9.collidepoint(event.pos):
                    if (difficulte == 4):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_4x4, sol_lvl9_4x4)
                    if (difficulte == 5):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_5x5, sol_lvl9_5x5)
                    if (difficulte == 6):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_6x6, sol_lvl9_6x6)
                    if (difficulte == 7):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_7x7, sol_lvl9_7x7)
                    if (difficulte == 8):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_8x8, sol_lvl9_8x8)
                    if (difficulte == 9):
                        from Futoshiki import def_Futoshiki
                        def_Futoshiki(difficulte, lvl9_9x9, sol_lvl9_9x9)



            pygame.display.flip()




