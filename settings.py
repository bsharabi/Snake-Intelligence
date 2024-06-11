import os
import sys
import random
from pygame import *
import pygame as pg
from collections import deque
from api.direction import Direction ,Point # Assuming Direction is defined in api.direction
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np

# Screen resolution and frame rate
RES = WIDTH, HEIGHT = (640, 480)
FPS = 40

# RGB color definitions
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


# Game settings
BLOCK_SIZE = 20

# Directory paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

# AI settings
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001
LR = 0.001


AI = os.path.join(CURRENT_DIR,"ai")
GAME = os.path.join(CURRENT_DIR,"game")



