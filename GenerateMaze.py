import random

import os
os.system('color')
from termcolor import colored

def generate_maze(n):
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    return maze