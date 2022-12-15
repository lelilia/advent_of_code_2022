"""
Advent of Code 2022
--- Day 14: Regolith Reservoir ---
"""


def get_input(filename):
    with open(filename, "r") as f:
        return f.read()


def create_blocked(input):
    blocked = {}
    max_x = 0
    for line in input.split("\n"):
        stones = [[int(x) for x in path.split(",")] for path in line.split(" -> ")]

        max_x = max(max_x, max([x for _, x in stones]))
        blocked[stones[0][0], stones[0][1]] = True
        for i in range(1, len(stones)):
            start_x, start_y = stones[i - 1]
            stop_x, stop_y = stones[i]
            while start_x != stop_x or start_y != stop_y:
                if start_x != stop_x:
                    start_x += abs(start_x - stop_x) // (stop_x - start_x)
                else:
                    start_y += abs(start_y - stop_y) // (stop_y - start_y)
                blocked[start_x, start_y] = True

    return blocked, max_x


def solve_1(input):
    blocked, max_y = create_blocked(input)
    print(max_y)
    stone = 0
    y = 0
    while y < max_y:
        x = 500
        y = 0
        while True:
            if y == max_y:
                return stone
            # down
            if (x, y + 1) not in blocked:
                y += 1
            # down left
            elif (x - 1, y + 1) not in blocked:
                x -= 1
                y += 1
            # down right
            elif (x + 1, y + 1) not in blocked:
                x += 1
                y += 1
            else:
                # print(x,y)
                blocked[x, y] = True
                break
        # print(stone, x, y)
        stone += 1
    return stone


def solve_2(input):
    blocked, max_y = create_blocked(input)
    max_y = max_y + 2
    stone = 0
    y = 0
    while True:
        x = 500
        y = 0
        while True:

            # down
            if (x, y + 1) not in blocked and y + 1 < max_y:
                y += 1
            # down left
            elif (x - 1, y + 1) not in blocked and y + 1 < max_y:
                x -= 1
                y += 1
            # down right
            elif (x + 1, y + 1) not in blocked and y + 1 < max_y:
                x += 1
                y += 1
            else:
                if x == 500 and y == 0:
                    return stone + 1
                blocked[x, y] = True
                break
        stone += 1
    return stone + 1


input = get_input("testinput14")
input = get_input("input14")

print("Part 1:", solve_1(input))
print("Part 2:", solve_2(input))
