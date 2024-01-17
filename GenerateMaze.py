import random


START = 'S'
END = 'E'
WALL = '▓'
OPEN_SPACE = '◌'
PATH_MARK = '•'

def generate_maze(n):
    maze = [[WALL if random.random() < 0.25 else OPEN_SPACE for _ in range(n)] for _ in range(n)]
    maze[0][0] = START
    maze[-1][-1] = END
    return maze