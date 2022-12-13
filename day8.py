import numpy as np

grid = np.loadtxt("testinput8", dtype=int)

with open("input8") as f:
    input = f.readlines()


grid = np.array([[int(x) for x in list(line.strip())] for line in input])

visible = grid.shape[0] * 2 + grid.shape[1] * 2 - 2


seen = {}

n, m = grid.shape

for i in range(n):
    highest = grid[i, 0]
    seen[i, 0] = True
    for j in range(1, m):
        if grid[i, j] > highest:
            seen[i, j] = True
            highest = grid[i, j]

for i in range(n - 1, -1, -1):
    highest = grid[i, m - 1]
    seen[i, m - 1] = True
    for j in range(m - 1, -1, -1):
        if grid[i, j] > highest:
            seen[i, j] = True
            highest = grid[i, j]

for j in range(m):
    highest = grid[0, j]
    seen[0, j] = True
    for i in range(n):
        if grid[i, j] > highest:
            seen[i, j] = True
            highest = grid[i, j]

for j in range(m - 1, -1, -1):
    highest = grid[n - 1, j]
    seen[n - 1, j] = True
    for i in range(n - 1, -1, -1):
        if grid[i, j] > highest:
            seen[i, j] = True
            highest = grid[i, j]


print("Part 1:", len(seen))

# part 2

max_score = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        score = 1

        # up
        seeing = 0
        x = 1
        while i - x >= 0:
            seeing += 1
            if grid[i - x, j] >= grid[i, j]:
                break
            x += 1
        score *= seeing
        # down
        seeing = 0
        x = 1
        while i + x < n:
            seeing += 1
            if grid[i + x, j] >= grid[i, j]:
                break
            x += 1
        score *= seeing
        # left
        seeing = 0
        x = 1
        while j - x >= 0:
            seeing += 1
            if grid[i, j - x] >= grid[i, j]:
                break
            x += 1
        score *= seeing
        # right
        seeing = 0
        x = 1
        while j + x < m:
            seeing += 1
            if grid[i, j + x] >= grid[i, j]:
                break
            x += 1
        score *= seeing
        max_score = max(max_score, score)
print("Part 2:", max_score)
