"""
Advent of Code 2022
--- Day 1: Calorie Counting ---
"""

import numpy as np


def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()


def get_best_3(current_score, best_1, best_2, best_3):
    if current_score > best_3:
        if current_score > best_2:
            if current_score > best_1:
                best_1, best_2, best_3 = current_score, best_1, best_2
            else:
                best_2, best_3 = current_score, best_2
        else:
            best_3 = current_score
    return best_1, best_2, best_3


def solve(input):
    max_score = 0
    current_score = 0
    best_1 = best_2 = best_3 = 0
    for line in input:
        line = line.strip()
        if line == "":
            max_score = max(max_score, current_score)
            best_1, best_2, best_3 = get_best_3(current_score, best_1, best_2, best_3)
            current_score = 0
        else:
            current_score += int(line)
    max_score = max(max_score, current_score)
    best_1, best_2, best_3 = get_best_3(current_score, best_1, best_2, best_3)

    print("Part 1:", max_score)
    print("Part 2:", best_1 + best_2 + best_3)


solve(get_input("input1"))
