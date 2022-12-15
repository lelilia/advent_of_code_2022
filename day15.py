"""
Advend of Code 2022
--- Day 15: Beacon Exclusion Zone ---
"""


def get_input(filename):
    with open(filename, "r") as f:
        return f.read()


def solve_1(input, res_row=2000000):
    res_1 = {}
    for line in input.split("\n"):
        _, _, x, y, _, _, _, _, xb, yb = (
            line.replace("x=", "")
            .replace("y=", "")
            .replace(":", "")
            .replace(",", "")
            .split(" ")
        )
        x, y, xb, yb = [int(a) for a in [x, y, xb, yb]]

        max_distance = abs(x - xb) + abs(y - yb)
        if abs(y - res_row) <= max_distance:
            width = max_distance - abs(y - res_row)
            for i in range(x - width, x + width):
                res_1[i] = True
    return len(res_1)


def solve_2a(input, area=4000000):
    res_2 = {}
    for line in input.split("\n"):
        _, _, x, y, _, _, _, _, xb, yb = (
            line.replace("x=", "")
            .replace("y=", "")
            .replace(":", "")
            .replace(",", "")
            .split(" ")
        )
        x, y, xb, yb = [int(a) for a in [x, y, xb, yb]]
        max_distance = abs(x - xb) + abs(y - yb)

    for row in range(max(x - max_distance, 0), min(x + max_distance + 1, area)):
        for col in range(max(y - max_distance, 0), min(y + max_distance + 1, area)):
            if abs(x - row) + abs(y - col) > max_distance:
                continue
            res_2[row, col] = True

    for i in range(area):
        print(i)
        for j in range(area):
            if (i, j) not in res_2:
                print(i, j)
                return 4000000 * i + j

    #     if abs(y-res_row) <= max_distance:
    #         width = max_distance - abs(y - res_row)
    #         for i in range(x-width, x + width):
    #             res_1[i] = True
    # return len(res_1)


def solve_2(input, area=4000000):
    res_2 = {}
    map = {}
    for line in input.split("\n"):
        _, _, x, y, _, _, _, _, xb, yb = (
            line.replace("x=", "")
            .replace("y=", "")
            .replace(":", "")
            .replace(",", "")
            .split(" ")
        )
        x, y, xb, yb = [int(a) for a in [x, y, xb, yb]]
        max_distance = abs(x - xb) + abs(y - yb)
        map[x, y] = max_distance
        for row in range(x - max_distance - 1, x + max_distance + 2):
            res_2[row, y - (max_distance - x + row + 1)] = True
            res_2[row, y + (max_distance - x + row + 2)] = True

    print("len", len(res_2))
    count = 0
    for pair in res_2.keys():
        count += 1
        if count % 100000 == 0:
            print(count)

        if check_area(*pair, map):
            if pair[0] < 0 or pair[0] > area:
                continue
            if pair[1] < 0 or pair[1] > area:
                continue
            return 4000000 * pair[0] + pair[1]
        # res_2[x,y] = max_distance
        # for x  in range(area):
        #     print(x)
        #     for y in range(area):
        #         if check_area(x, y, res_2):
        #             return 4000000*x + y


def check_area(x, y, map):
    for key, value in map.items():
        if abs(x - key[0]) + abs(y - key[1]) <= value:
            return False
    return True


test_input = get_input("testinput15")
input = get_input("input15")


# print("Part 1:", solve_1(input))
print("here")
print("Part 2:", solve_2(input))

assert check_area(6, 8, {(8, 7): 9}) == False
