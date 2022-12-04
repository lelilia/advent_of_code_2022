"""
Advent of Code 2022
--- Day 2: Rock Paper Scissors ---
"""

OUTCOME_1 = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

OUTCOME_2 = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}


def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()


def solve(input):
    score_1 = 0
    score_2 = 0
    for line in input:
        line = line.strip()
        if line == "":
            continue
        score_1 += OUTCOME_1[line]
        score_2 += OUTCOME_2[line]

    print("Part 1:", score_1)
    print("Part 2:", score_2)


solve(get_input("input2"))
