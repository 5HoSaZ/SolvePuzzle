import numpy as np

# Initial state of the board
board = np.loadtxt("board.txt", dtype="int8")

# To keep track of the number of solutions
counter = 0

# Scan through the board to find the positions of the already filled boxes
# These boxes will not be changed during execution
filled_box_list = set((i, j) for i in range(9) for j in range(9) if board[i][j] > 0)


# To print a solution after filling the board
def print_solution():
    print(board)


# Conditions for backtracking
def bool_check(val, row, col):
    # Check with every element on top in the same column
    for i in range(row):
        if board[i][col] == val:
            return False

    # Check with every element to the left in the same row
    for j in range(col):
        if board[row][j] == val:
            return False

    # Check with every element in the same 3x3 sub box

    # The position of the sub box
    sub_I, sub_J = row // 3, col // 3

    # The relative position of the element in the sub box in (x, y)
    rel_i, rel_j = row % 3, col % 3

    # The relative position as boxes from left to right, top to bottom of the sub box
    # Ex:   | 1 | 2 | 3 |
    #       | 4 | 5 | 6 |
    #       | 7 | 8 | 9 |

    rel_box = rel_i * 3 + rel_j

    for box in range(rel_box):
        if board[box // 3 + sub_I * 3][box % 3 + sub_J * 3] == val:
            return False

    return True


def Try(row, col):
    # Use a global counter to keep tract of the number of solutions founded
    global counter

    # If the box is filled, check only its value
    if (row, col) in filled_box_list:
        if bool_check(board[row][col], row, col):
            if row == 8 and col == 8:
                print_solution()
                counter += 1
            elif col == 8:
                Try(row + 1, 0)
            else:
                Try(row, col + 1)

    # Otherwise, test for all possible numbers from 1 to 9
    else:
        for v in range(1, 10):
            if bool_check(v, row, col):
                board[row][col] = v
                if row == 8 and col == 8:
                    print_solution()
                    counter += 1
                elif col == 8:
                    Try(row + 1, 0)
                else:
                    Try(row, col + 1)


if __name__ == "__main__":
    Try(0, 0)
    print(counter)
