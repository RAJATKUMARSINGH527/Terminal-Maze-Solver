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