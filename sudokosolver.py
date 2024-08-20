import random
import sys

UNASSIGNED = 0
N = 9

class Puzzle:
    def __init__(self, values):
        self.values = values

easy_puzzles = [
    Puzzle([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
]

medium_puzzles = [
    Puzzle([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
]

hard_puzzles = [
    Puzzle([
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ])
]

def load_puzzle(difficulty_level):
    puzzles = None
    if difficulty_level == 1:
        puzzles = easy_puzzles
    elif difficulty_level == 2:
        puzzles = medium_puzzles
    elif difficulty_level == 3:
        puzzles = hard_puzzles
    else:
        raise ValueError("Invalid difficulty level!")

    rand_index = random.randint(0, len(puzzles) - 1)
    selected_puzzle = puzzles[rand_index]

    return selected_puzzle.values

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_safe(grid, row, col, num):
    for x in range(N):
        if grid[row][x] == num or grid[x][col] == num or grid[3 * (row // 3) + x // 3][3 * (col // 3) + x % 3] == num:
            return False
    return True

def solve_sudoku(grid):
    row, col = find_unassigned_location(grid)
    if row is None:
        return True

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = UNASSIGNED

    return False

def find_unassigned_location(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == UNASSIGNED:
                return row, col
    return None, None

if __name__ == "__main__":
    try:
        difficulty_level = int(input("Choose difficulty level (1: Easy, 2: Medium, 3: Hard): "))
        if difficulty_level < 1 or difficulty_level > 3:
            raise ValueError
    except ValueError:
        print("Invalid difficulty level. Please choose 1, 2, or 3.")
    else:
        print("Loading puzzle...")
        try:
            grid = load_puzzle(difficulty_level)
        except ValueError as e:
            print(f"Error loading puzzle: {e}")
        else:
            print("Stored Puzzle:")
            print_grid(grid)

            if solve_sudoku(grid):
                print("Solved Puzzle:")
                print_grid(grid)
            else:
                print("No solution exists")
    
    # Wait for user input before closing
    if sys.platform.startswith('win'):
        input("Press Enter to exit...")
