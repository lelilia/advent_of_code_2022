"""
Advent of Code 2022
--- Day 10: Cathode-Ray Tube ---
"""


def get_input(file):
    with open(file, "r") as f:
        return f.read()


def solve(input):
    X = 1
    clock = 1
    part_1 = 0
    part_2 = ""
    crt = 0
    for line in input.replace(" ", "\n").split("\n"):
        if (clock - 1) % 40 == 0:
            crt = 0
            part_2 += "\n"
        if abs(X - crt) <= 1:
            part_2 += "#"
        else:
            part_2 += "."
        if not line.isalpha():
            value = int(line)
            X += value
        clock += 1
        crt += 1
        if clock % 40 == 20:
            part_1 += clock * X
    return part_1, part_2


input = get_input("input10")

part_1, part_2 = solve(input)
print("Part 1:", part_1)
print("Part 2:\n", part_2)
