import numpy as np
import matplotlib.pyplot as plt
import random

def make_board(n):
    nutrients = np.random.randint(0, 10, size=(n, n))
    plt.imshow(nutrients, cmap='YlGn')
    plt.colorbar(label="Nutrient level")
    plt.show()
    return nutrients

def get_neighbours(board, x, y):
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    coords = [(x + dx, y + dy) for dx,dy in directions
              if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0])]
    return ((board[nx][ny], nx, ny) for nx, ny in coords)

def move(board):
    rows = len(board)
    cols = len(board[0])

    memo = {}  # (x,y)

    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        start_val = board[x][y]
        best_sum = start_val
        best_path = [(x, y)]

        for newval, nx, ny in get_neighbours(board, x, y):
            if newval > start_val:
                sub_sum, sub_path = dfs(nx, ny)
                new_total = start_val + sub_sum

                if new_total > best_sum:
                    best_sum = new_total
                    best_path = [(x, y)] + sub_path

        memo[(x, y)] = (best_sum, best_path)
        return memo[(x, y)]

    global_best_sum = 0
    global_best_path = []

    for row in range(rows):
        for col in range(cols):
            path_sum, path = dfs(row, col)
            if path_sum > global_best_sum:
                global_best_sum = path_sum
                global_best_path = path

    return global_best_sum, global_best_path

def draw_path(board, path):
    plt.figure(figsize=(6,6))
    plt.imshow(board, cmap='YlGn')
    plt.colorbar(label="Nutrient level")

    xs = [y for x, y in path]   
    ys = [x for x, y in path]

    plt.plot(xs, ys, color="red", linewidth=2, marker="o")
    plt.title("Optimal Path")
    plt.gca().invert_yaxis()  
    plt.show()

board = make_board(10)
best_sum, best_path = move(board)

print("Best score:", best_sum)
print("Path:", best_path)

draw_path(board, best_path)
