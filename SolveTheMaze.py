#Solve the Maze Function
def solve_maze(maze):
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()

    if find_path(maze, start_position, end_position, visited):
        return maze
    else:
        return None