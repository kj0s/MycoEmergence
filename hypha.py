import numpy as np
import matplotlib.pyplot as plt
import random

ENERGY_START = 5
ENERGY_DEDUCT_COST = 1

def make_board(n):
    nutrients = np.random.randint(0, 10, size=(n, n))
    plt.imshow(nutrients, cmap='YlGnBu')
    plt.colorbar(label="Nutrient level")
    plt.show()
    return nutrients

def get_neighbours(board, x, y):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    coords = [(x + dx, y + dy) for dx,dy in directions
              if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0])]
    return ((board[nx][ny], nx, ny) for nx, ny in coords)



def move(board):
    rows = random.randint(0, len(board)-1)
    cols = random.randint(0, len(board[0])-1)
    start = board[rows][cols]
    stack = [(start, rows, cols)]
    path = [(rows, cols)]
    energy = ENERGY_START
    while stack and energy > 0:
        ogval, ox, oy = stack.pop()
        possible = []
        for newval, nx, ny in get_neighbours(board, ox, oy):
            if (nx, ny) not in path:
                possible.append((newval, nx, ny))
        if not possible:
            break
        best = sorted(possible, key=lambda x: x[0], reverse=True)[0]
        path.append((best[1], best[2]))
        energy += best[0] - ENERGY_DEDUCT_COST
        stack.append((best[0], best[1], best[2]))
    return path


def draw_path(board, path):
    plt.figure(figsize=(6,6))
    plt.imshow(board, cmap='YlGnBu')
    plt.colorbar(label="Nutrient level")

    xs = [y for x, y in path]
    ys = [x for x, y in path]

    plt.plot(xs, ys, color="pink", linewidth=2, marker="o")
    plt.title("Optimal Path")
    plt.gca().invert_yaxis()
    plt.show()

board = make_board(10)
path = move(board)

print("Path:", path)

draw_path(board, path)
