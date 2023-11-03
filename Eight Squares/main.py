import copy
from heapq import heappush, heappop

# we have defined 3 x 3 board therefore n = 3..
n = 3

# bottom, left, top, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]


class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)

    # remove minimum element
    def pop(self):
        return heappop(self.heap)

    # Check if queue is empty
    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        # parent node of current node
        self.parent = parent

        # matrix
        self.mat = mat

        # position of empty tile
        self.empty_tile_pos = empty_tile_pos

        # Total Misplaced tiles
        self.cost = cost

        # Number of moves so far
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost


# Calculate number of non-blank tiles not in their goal position
def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if (mat[i][j]) and (mat[i][j] != final[i][j]):
                count += 1
    return count


def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> Node:
    new_mat = copy.deepcopy(mat)
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Set number of misplaced tiles
    cost = calculateCost(new_mat, final)
    new_node = Node(parent, new_mat, new_empty_tile_pos, cost, level)
    return new_node


# print the N x N matrix
def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end=" ")
        print()


def isLegalMove(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def printPath(root):
    if root is None:
        return

    printPath(root.parent)
    printMatrix(root.mat)
    print()


def solve(initial, empty_tile_pos, final):
    pq = PriorityQueue()

    # Create the root node
    cost = calculateCost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)

    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()

        # If minimum is the answer node
        if minimum.cost == 0:
            # Print the path from root to destination;
            printPath(minimum)
            return

        # Produce all possible children
        for i in range(4):
            new_tile_pos = [
                minimum.empty_tile_pos[0] + row[i],
                minimum.empty_tile_pos[1] + col[i],
            ]

            if isLegalMove(new_tile_pos[0], new_tile_pos[1]):
                # Create a child node
                child = newNode(
                    minimum.mat,
                    minimum.empty_tile_pos,
                    new_tile_pos,
                    minimum.level + 1,
                    minimum,
                    final,
                )

                # Add child to list of live nodes
                pq.push(child)


# Driver Code
# 0 represents the blank space
# Initial state
initial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Final State
final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Blank tile position during start state
empty_tile_pos = [2, 1]

# Function call
solve(initial, empty_tile_pos, final)
