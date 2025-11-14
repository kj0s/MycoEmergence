import numpy as np
import matplotlib.pyplot as plt
import random

ENERGY_START = 5
ENERGY_DEDUCT_COST = 1
EPSILON = 0.2

def make_board(n):
    nutrients = np.random.randint(0, 10, size=(n, n))
    plt.imshow(nutrients, cmap='Greys')
    plt.colorbar(label="Nutrient level")
    # plt.show()
    return nutrients

def get_neighbours(board, x, y):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    coords = [(x + dx, y + dy) for dx,dy in directions
              if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0])]
    return ((board[nx][ny], nx, ny) for nx, ny in coords)



def move(board):
    rows = random.randint(0, len(board)-1)
    cols = random.randint(0, len(board[0])-1)
    stack = [(board[rows][cols], rows, cols, [(rows, cols)], ENERGY_START)]
    finished_paths = []
    visited = set([(rows, cols)])

    while stack:
        val, x, y, path, energy = stack.pop()
        possible = [(v, nx, ny) for v, nx, ny in get_neighbours(board, x, y)
                    if (nx, ny) not in visited]

        if not possible or energy <= 0:
            finished_paths.append(path)
            continue

        best = sorted(possible, key=lambda x: x[0], reverse=True)

        # main
        new_path = path.copy()
        new_path.append((best[0][1], best[0][2]))
        new_energy = energy + best[0][0] - ENERGY_DEDUCT_COST
        visited.add((best[0][1], best[0][2]))
        stack.append((best[0][0], best[0][1], best[0][2], new_path, new_energy))

        # branch
        if len(best) > 1 and random.random() < EPSILON:
            second_path = path.copy()
            second_path.append((best[1][1], best[1][2]))
            second_energy = energy + best[1][0] - ENERGY_DEDUCT_COST
            visited.add((best[1][1], best[1][2]))
            stack.append((best[1][0], best[1][1], best[1][2], second_path, second_energy))

    return finished_paths

def draw_paths(board, paths):
    plt.figure(figsize=(8,8))
    plt.imshow(board, cmap='Greys')
    plt.colorbar(label="Nutrient level")
    plt.gca().invert_yaxis()

    colors = plt.cm.viridis(np.linspace(0, 1, len(paths)))
    for path, color in zip(paths, colors):
        xs = [y for x, y in path]
        ys = [x for x, y in path]
        plt.plot(xs, ys, color=color, linewidth=2, marker="x")

    plt.title("Branching Paths")
    plt.show()


board = make_board(40)
paths = move(board)
draw_paths(board, paths)
