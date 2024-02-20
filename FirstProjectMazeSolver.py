import random

import os
os.system('color')
from termcolor import colored

from collections import deque

def generate_maze(n):
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    maze[0][0] = "S"
    maze[n-1][n-1] = "E"
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
        
#using Backtracking
# def find_path(maze, current_position, end_position, visited):
#     if current_position == end_position:
#         return True

#     row, col = current_position

#     if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (maze[row][col] == "◌" or maze[row][col] == "S" or maze[row][col] == "E") and (row, col) not in visited:
#         visited.add((row, col))
#         maze[row][col] = "◍"

#         # Check in all four directions (up, down, left, right)
#         if (find_path(maze, (row - 1, col), end_position, visited) or
#             find_path(maze, (row + 1, col), end_position, visited) or
#             find_path(maze, (row, col - 1), end_position, visited) or
#             find_path(maze, (row, col + 1), end_position, visited)):
#             return True

#         maze[row][col] = "◌"  # Backtrack if no path found
        
#     return False

# def solve_maze(maze):
#     start_position = (0, 0)
#     end_position = (len(maze) - 1, len(maze[0]) - 1)
#     visited = set()

#     if find_path(maze, start_position, end_position, visited):
#         return maze
#     else:
#         return None

#using BFS 
def find_path(maze, start, goal):
    # print(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == goal:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and (maze[new_x][new_y] == "◌" or maze[new_x][new_y] == "S" or maze[new_x][new_y] == "E"):
                queue.append(((new_x, new_y), path + [current]))

    return None

# solve maze using BFS
def solve_maze(maze):
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)
    

    path=find_path(maze, start_position, end_position)
    if path:
        for t in path:
            row,col=t[0],t[1]
            maze[row][col]  =  "◍"
        return True
    return False        
              

   
def main():
    
    print(colored("\nLet's Start the Maze Solver Game","red","on_white"))
    n = int(input("\nEnter the size of the maze (n*n) :-  "))
    print()
    maze = generate_maze(n) 
    print_maze(maze)     
    # print(maze)
    while True:
    
        print("\n1. Print the Path ")
        print("2. Generate another Maze ")
        print("3. Exit the Game ❌\n")
        
        players_choice=int(input("Enter Your Choice (1/2/3)❓❓:-  "))
        
        # if players_choice==1:
            
        #     solution = solve_maze(maze)
        #     # print(maze)
            
        #     if solution:
        #         print(colored("\nPath Found \n","green","on_white"))
        #         print_maze(solution)
        #     else:
        #         print(colored("\nNo path found \n","red","on_white"))   
        
        if players_choice==1:
            
            solution = solve_maze(maze)
            # print(maze)
            
            if solution:
                print(colored("\nPath Found \n","green","on_white"))
                print_maze(maze)
            else:
                print(colored("\nNo path found \n","red","on_white"))        
            
        elif players_choice==2:
            n = int(input("\nEnter the size of the maze (n*n) :-  "))
            maze = generate_maze(n)
        
            # print(maze)
        
            print(colored("\nMaze Generated 👇","blue"))
            print()
            print_maze(maze)

            
        elif players_choice == 3:
            
            print(colored("\nThank you for playing the Maze Solver Game.\n","black","on_light_green"))
            break
        
        else:
            players_choice=int(input("Enter Your Choice (1/2/3)❓❓:-  "))
            
if __name__ == "__main__":
    main()