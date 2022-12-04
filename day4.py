"""
Advent of Code 2022
--- Day 4: Camp Cleanup ---
"""

with open("input4", "r") as f:
    input = f.readlines()

count_1 = 0
count_2 = 0

for line in input:
    a_1, a_2, b_1, b_2 = [int(x) for y in line.split(",") for x in y.split("-")]

    if a_1 <= b_1 and a_2 >= b_2 or b_1 <= a_1 and b_2 >= a_2:
        count_1 += 1
    if a_1 <= b_1 <= a_2 or b_1 <= a_1 <= b_2:
        count_2 += 1

print("Part 1:", count_1)
print("Part 2:", count_2)
