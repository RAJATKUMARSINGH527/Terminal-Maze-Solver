# Import necessary modules
import random  # For generating random numbers
import os  # For interacting with the operating system
os.system('color')  # Set color mode for the terminal (Windows)
from termcolor import colored  # For colored text output in the terminal
from collections import deque  # For implementing queue with efficient appends and pops from both ends

# Function to generate a maze of size n x n
def generate_maze(n):
    # Initialize the maze with randomly placed walls ('▓') and empty spaces ('◌')
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    # Set start position ('S') at top left corner
    maze[0][0] = "S"
    # Set end position ('E') at bottom right corner
    maze[n-1][n-1] = "E"
    return maze

# Function to print the maze with colored text
def print_maze(maze):
    # Get the dimensions of the maze
    total_rows = total_columns = len(maze)
    # Iterate through each cell in the maze
    for row in range(total_rows):
        for col in range(total_columns):
            # Print start position ('S') in green on black background
            if (row == 0 and col == 0):
                print(colored(" S ","green","on_black"),end="")
            # Print end position ('E') in green on black background
            elif (row == total_rows-1 and col == total_columns-1):
                print(colored(" E ","green","on_black"),end="")
            # Print empty space ('◌') in blue on white background
            elif maze[row][col] == "◌":
                print(colored(" ◌ ","blue","on_white"),end="")
            # Print wall ('▓') in red on white background
            elif maze[row][col] == "▓":
                print(colored(" ▓ ","red","on_white"),end="")
            # Print path ('◍') in green on white background
            elif maze[row][col] == "◍":
                print(colored(" ◍ ","green","on_white"),end="")
        print()  # Move to the next line after printing each row

# Function to find a path in the maze using Breadth First Search (BFS)
def find_path(maze, start, goal):
    # Define possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Initialize a queue with the start position and an empty path
    queue = deque([(start, [])])
    # Initialize a set to keep track of visited cells
    visited = set()

    # Iterate until the queue is empty
    while queue:
        current, path = queue.popleft()  # Get the current position and path from the queue
        x, y = current  # Extract row and column indices from the current position

        # If the current position is the goal, return the path to reach it
        if current == goal:
            return path + [current]

        # If the current position has been visited before, continue to the next iteration
        if current in visited:
            continue

        # Mark the current position as visited
        visited.add(current)

        # Explore each direction from the current position
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if the new position is within the maze boundaries and is a valid move (empty space, start, or end)
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and (maze[new_x][new_y] == "◌" or maze[new_x][new_y] == "S" or maze[new_x][new_y] == "E"):
                # Add the new position and the current path to the queue
                queue.append(((new_x, new_y), path + [current]))

    # If no path is found, return None
    return None

# Function to solve the maze using BFS
def solve_maze(maze):
    # Define the start and end positions
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)

    # Find a path from the start to the end position
    path = find_path(maze, start_position, end_position)
    
    # If a path is found, mark it in the maze and return True
    if path:
        for t in path:
            row,col=t[0],t[1]
            maze[row][col]  =  "◍"  # Mark the path with '◍'
        return True
    # If no path is found, return False
    return False

# Main function to run the maze solver game
def main():
    # Print welcome message
    print(colored("\nLet's Start the Maze Solver Game","red","on_white"))
    # Ask user for maze size
    n = int(input("\nEnter the size of the maze (n*n) :-  "))
    print()
    # Generate the initial maze
    maze = generate_maze(n) 
    # Print the initial maze
    print_maze(maze)
    
    # Main game loop
    while True:
        # Print menu options
        print("\n1. Print the Path ")
        print("2. Generate another Maze ")
        print("3. Exit the Game ❌\n")
        # Get user's choice
        players_choice = int(input("Enter Your Choice (1/2/3)❓❓:-  "))
        
        # Option to print the path in the maze
        if players_choice == 1:
            solution = solve_maze(maze)
            if solution:
                print(colored("\nPath Found \n","green","on_white"))
                print_maze(maze)
            else:
                print(colored("\nNo path found \n","red","on_white"))        
            
        # Option to generate another maze
        elif players_choice == 2:
            n = int(input("\nEnter the size of the maze (n*n) :-  "))
            maze = generate_maze(n)
            print(colored("\nMaze Generated 👇","blue"))
            print()
            print_maze(maze)
            
        # Option to exit the game
        elif players_choice == 3:
            print(colored("\nThank you for playing the Maze Solver Game.\n","black","on_light_green"))
            break
        
        # Handle invalid choices
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
