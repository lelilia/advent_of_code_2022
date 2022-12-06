"""
Advent of Code 2022
--- Day 6: Tuning Trouble ---
"""

with open("input6", "r") as f:
    input = f.read()


def solve(string, n=4):
    i = n
    while i < len(string):
        if len(set(string[i - n : i])) == n:
            return i
        i += 1


print("Part 1:", solve(input))
print("Part 2:", solve(input, 14))

assert (res := solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) == 7, f"{res}"
assert (res := solve("bvwbjplbgvbhsrlpgdmjqwftvncz")) == 5, f"{res}"
