"""
Advent of Code 2022
"""

with open("input3") as f:
    input = f.readlines()


def get_value(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def find_item(bag):
    size = len(bag) // 2
    compartment_1, compartment_2 = bag[:size], bag[size:]
    return list(set(compartment_1).intersection(set(compartment_2)))[0]


def find_badge(bags):
    bag_1, bag_2, bag_3 = [bag.strip() for bag in bags]
    return list(set(bag_1).intersection(bag_2).intersection(bag_3))[0]


def solve(elves):
    part_1 = part_2 = 0
    for i in range(len(elves)):
        item = find_item(elves[i])
        part_1 += get_value(item)
        if i % 3 == 0:
            badge = find_badge(elves[i : i + 3])
            part_2 += get_value(badge)
    return part_1, part_2


solution_1, solution_2 = solve(input)

print("Part 1:", solution_1)
print("Part 2:", solution_2)
