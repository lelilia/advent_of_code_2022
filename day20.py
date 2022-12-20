"""
Advend of Code 2022
--- Day 20: Grove Positioning System ---
"""


def get_input(file):
    with open(file) as f:
        input = f.read()
    return [(i,int(x)) for i, x in enumerate(input.split("\n"))]


def solve_1(input):
    order = input.copy()
    ring = input.copy()
    length = len(ring)
    mod = length - 1

    while order:
        curr = order.pop(0)
        index = ring.index(curr)
        ring.remove(curr)
        ring.insert((index + curr[1]) % mod, curr[1])
        # print(curr, index, ring)

    zero_index = ring.index(0)
    return ring[(zero_index + 1000) % length] + ring[(zero_index + 2000) % length] + ring[(zero_index + 3000) % length]


def solve_2(input):
    input = [(i, 811589153 * x) for i, x in input]
    ring = input.copy()
    length = len(ring)
    mod = length - 1
    for times in range(10):
        order = input.copy()
        while order:
            curr = order.pop(0)
            index = ring.index(curr)
            ring.remove(curr)
            if times < 9:
                ring.insert((index + curr[1]) % mod, curr)
            else:
                ring.insert((index + curr[1]) % mod, curr[1])

    zero_index = ring.index(0)
    return ring[(zero_index + 1000) % length] + ring[(zero_index + 2000) % length] + ring[(zero_index + 3000) % length]

input = get_input("input20")

print("Part 1:", solve_1(input))

print("Part 2:", solve_2(input))