#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:15:18 2024

@author: jameslloyd
"""

WIN_WIDTH = 800
WIN_HEIGHT = 600
scaling_factor = 2

TILESIZE = 32
TILESIZE2 = 64
FPS = 60

HEALTH_LAYER =6
PLAYER_LAYER = 5
WEAPON_LAYER = 4
ENEMY_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1

PLAYER_STEPS = 3
ENEMY_STEPS = 1
BULLET_STEPS= 6

ENEMY_HEALTH = 6
PLAYER_HEALTH= 10

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255) 

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B........TTT...............CC............................B',
    'B.........T..............................................B',
    'B.E.......T...E..........A...............................B',
    'B....A................................................T..B',
    'B............................................TTT.........B',
    'B........T.RRC............................A...........TT.B',
    'B........T.........A.....................A.......RR....E.B',
    'B..TT.....P.W.............................A..............B',
    'BE............E........................................C.B',
    'B.........................................A.TTTTT......RRB',
    'B..E......................RR...........................RRB',
    'BE..............C.......................................RB',
    'B......................................CC................B',
    'B........................................................B',
    'B......A.................................................B',
    'B..........................R.............................B',
    'B..........................R.............................B',
    'B........................CCR...................CC....E...B',
    'B..........................R.............................B',
    'B........RRRRRR..RRRRRRRRRRR.............................B',
    'B........RRRRRRR...RRRRRRRRR.............................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    ]
