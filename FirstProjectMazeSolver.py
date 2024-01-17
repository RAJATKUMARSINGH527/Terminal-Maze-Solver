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


def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def find_path(maze, current_position, end_position, visited):
    if current_position == end_position:
        return True

    row, col = current_position

    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == OPEN_SPACE and (row, col) not in visited:
        visited.add((row, col))
        maze[row][col] = PATH_MARK

        # Check in all four directions (up, down, left, right)
        if (find_path(maze, (row - 1, col), end_position, visited) or
            find_path(maze, (row + 1, col), end_position, visited) or
            find_path(maze, (row, col - 1), end_position, visited) or
            find_path(maze, (row, col + 1), end_position, visited)):
            return True

        maze[row][col] = OPEN_SPACE  # Backtrack if no path found

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
    n = int(input("Enter the size of the maze (n): "))
    maze = generate_maze(n)

    print("Maze Generated:")
    print_maze(maze)

    solution = solve_maze(maze)

    if solution:
        print("\nPath Found:")
        print_maze(solution)
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()
