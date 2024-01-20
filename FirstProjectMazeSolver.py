import random

import os
os.system('color')
from termcolor import colored

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
        

def find_path(maze, current_position, end_position, visited):
    if current_position == end_position:
        return True

    row, col = current_position

    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (maze[row][col] == "◌" or maze[row][col] == "S" or maze[row][col] == "E") and (row, col) not in visited:
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

def solve_maze(maze):
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()

    if find_path(maze, start_position, end_position, visited):
        return maze
    else:
        return None

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
        
        if players_choice==1:
            
            solution = solve_maze(maze)
            # print(maze)
            
            if solution:
                print(colored("\nPath Found \n","green","on_white"))
                print_maze(solution)
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
            
            print("\nThank you for playing the Maze Solver Game.\n")
            break
        
        else:
            players_choice=int(input("Enter Your Choice (1/2/3)❓❓:-  "))
            
if __name__ == "__main__":
    main()