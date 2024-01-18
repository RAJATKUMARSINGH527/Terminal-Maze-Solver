import random

import os
os.system('color')
from termcolor import colored

def generate_maze(n):
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    return maze


def print_maze(maze):
    
    total_rows = total_columns = len(maze)
    for row in range(total_rows):
        for col in range(total_columns):
            if (row == 0 and col == 0):
                print(colored(" S ","green","on_black"),end="")
            elif (row == total_rows-1 and col == total_columns-1):
                print(colored(" E ","green","on_black"),end="")
            elif maze[row][col] == "◌":
                print(colored(" ◌ ","blue","on_white"),end="")
            elif maze[row][col] == "▓":
                print(colored(" ▓ ","red","on_white"),end="")
            elif maze[row][col] == "◍":
                print(colored(" ◍ ","green","on_white"),end="")
        print()
        

def find_path(maze, current_position, end_position, visited):
    if current_position == end_position:
        return True

    row, col = current_position

    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == "◌" and (row, col) not in visited:
        visited.add((row, col))
        maze[row][col] = "◍"

        # Check in all four directions (up, down, left, right)
        if (find_path(maze, (row - 1, col), end_position, visited) or
            find_path(maze, (row + 1, col), end_position, visited) or
            find_path(maze, (row, col - 1), end_position, visited) or
            find_path(maze, (row, col + 1), end_position, visited)):
            return True

        maze[row][col] = "◌"  # Backtrack if no path found
        return False
    return False

def solve_maze(maze):
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()

    if find_path(maze, start_position, end_position, visited):
        return maze
    else:
        return None

def main():
    n = int(input("\nEnter the size of the maze (n): "))
    maze = generate_maze(n)
    
    # print(maze)
    
    print("\nMaze Generated ⬇️")
    print()
    print_maze(maze)

    solution = solve_maze(maze)
    # print(maze)
   
    if solution:
        print("\nPath Found 😃\n")
        print_maze(solution)
    else:
        print("\nNo path found ☹️\n")

if __name__ == "__main__":
    main()