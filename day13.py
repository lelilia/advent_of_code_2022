"""
Advent of Code 2022
--- Day 13: Distress Signal ---
"""


def get_input(file):
    with open(file, "r") as f:
        return f.read()


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return
    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])

    else:
        if len(left) == 0:
            if len(right) == 0:
                return
            return True
        if len(right) == 0:
            return False

        curr_left = left.pop(0)
        curr_right = right.pop(0)

        res = compare(curr_left, curr_right)
        if res is None:
            return compare(left, right)
        else:
            return res


def solve_1(input):
    part_1 = 0
    for i, pair in enumerate(input.split("\n\n")):
        left, right = pair.split("\n")
        res = compare(eval(left), eval(right))
        if res:
            part_1 += i + 1
    return part_1


def solve_2(input):
    input = input.replace("\n\n", "\n")
    keys2 = [eval(x) for x in input.split("\n")]
    keys6 = [eval(x) for x in input.split("\n")]

    s2 = 1
    s6 = 2

    for key in keys2:
        if compare(key, [[2]]):
            s2 += 1
    for key in keys6:
        if compare(key, [[6]]):
            s6 += 1
    return s2 * s6


input = get_input("input13")
print("Part 1:", solve_1(input))

print("Part 2:", solve_2(input))
exit()

assert compare([], [1]) == True
assert compare([1], []) == False
assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == True
assert compare([9], [[9, 1]]) == True
assert compare([[9, 1]], [9]) == False
assert compare([[1], [2, 3, 4]], [[1], 4]) == True
assert compare([9], [[8, 7, 6]]) == False
assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == True
assert compare([7, 7, 7, 7], [7, 7, 7]) == False
assert compare([], [3]) == True
assert compare([[[]]], [[]]) == False
assert (
    compare([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
    == False
)
assert solve_1(get_input("testinput13")) == 13
