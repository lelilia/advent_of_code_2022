"""
Advent of Code 2022
--- Day 9: Rope Bridge ---
"""

import math


def get_input(file):
    with open(file, "r") as f:
        return f.read()


def touching(hx, hy, tx, ty):
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def follow(hx, hy, tx, ty):
    if touching(hx, hy, tx, ty):
        return tx, ty

    if hx == tx:
        ty = (hy + ty) // 2
    elif hy == ty:
        tx = (hx + tx) // 2
    else:
        if abs(tx - hx) == 1:
            tx = hx
        else:
            tx = (hx + tx) // 2
        if abs(ty - hy) == 1:
            ty = hy
        else:
            ty = (hy + ty) // 2

    return tx, ty


def solve(input):
    visited_1 = {}
    visited_9 = {}
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in input.split("\n"):
        direction, steps = line.split(" ")
        if direction == "R":
            d_x = 1
            d_y = 0
        elif direction == "L":
            d_x = -1
            d_y = 0
        elif direction == "U":
            d_x = 0
            d_y = 1
        elif direction == "D":
            d_x = 0
            d_y = -1
        for _ in range(int(steps)):
            x[0] += d_x
            y[0] += d_y

            for i in range(1, 10):
                x[i], y[i] = follow(x[i - 1], y[i - 1], x[i], y[i])
            visited_1[x[1], y[1]] = True
            visited_9[x[9], y[9]] = True

    return len(visited_1), len(visited_9)


input = get_input("input9")
res_1, res_2 = solve(input)
print("Part 1:", res_1)
print("Part 2:", res_2)

assert touching(0, 0, 0, 0) == True
assert touching(1, 0, 0, 0) == True
assert touching(1, 1, 0, 0) == True
assert touching(1, 2, 0, 0) == False

assert follow(0, 0, 0, 0) == (0, 0)
assert follow(2, 0, 0, 0) == (1, 0)
assert follow(0, 2, 0, 0) == (0, 1)
assert follow(2, 3, 2, 1) == (2, 2)
assert follow(1, 2, 0, 0) == (1, 1)
assert follow(2, 1, 0, 0) == (1, 1)
assert follow(2, 2, 0, 0) == (1, 1)
assert follow(4, 8, 5, 6) == (4, 7)
