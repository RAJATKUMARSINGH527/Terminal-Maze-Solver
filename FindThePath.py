#using BFS 

from collections import deque
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




# #Path Find Function
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

#         maze[row][col] = "◌"  # Backtrack if no path foundd
        
#     return False
