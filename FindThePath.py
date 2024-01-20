#Path Find Function
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
