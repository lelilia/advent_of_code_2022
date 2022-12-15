"""
Advent of Code 2022
--- Day 11: Monkey in the Middle ---
"""


def get_input(filename):
    with open(filename) as f:
        return f.read()


class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.items = items
        self.operation = operation.replace("new =", "")
        self.test = test
        self.if_false = if_false
        self.if_true = if_true
        self.inspect_counter = 0
        self.div = None

    def set_div(self, div):
        self.div = div

    def inspect_1(self):
        self.inspect_counter += 1
        old = self.items.pop(0)
        item = eval(self.operation)
        item //= 3
        if item % self.test == 0:
            return self.if_true, item
        else:
            return self.if_false, item

    def inspect_2(self):
        self.inspect_counter += 1
        old = self.items.pop(0)
        item = eval(self.operation)
        item %= self.div
        if item % self.test == 0:
            return self.if_true, item
        else:
            return self.if_false, item

    def get_item(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0


monkeys = [
    Monkey(0, [93, 54, 69, 66, 71], "new = old * 3", 7, 7, 1),
    Monkey(1, [89, 51, 80, 66], "new = old * 17", 19, 5, 7),
    Monkey(2, [90, 92, 63, 91, 96, 63, 64], "new = old + 1", 13, 4, 3),
    Monkey(3, [65, 77], "new = old + 2", 3, 4, 6),
    Monkey(4, [76, 68, 94], "new = old * old", 2, 0, 6),
    Monkey(5, [86, 65, 66, 97, 73, 83], "new = old + 8", 11, 2, 3),
    Monkey(6, [78], "new = old + 6", 17, 0, 1),
    Monkey(7, [89, 57, 59, 61, 87, 55, 55, 88], "new = old + 7", 5, 2, 5),
]

# Part 1
for round in range(20):
    for monkey in monkeys:
        while monkey.has_items():
            target, item = monkey.inspect_1()
            monkeys[target].get_item(item)

res_1 = sorted([m.inspect_counter for m in monkeys])[-2:]
print("Part 1:", res_1[0] * res_1[1])

# Part 2


monkeys = [
    Monkey(0, [93, 54, 69, 66, 71], "new = old * 3", 7, 7, 1),
    Monkey(1, [89, 51, 80, 66], "new = old * 17", 19, 5, 7),
    Monkey(2, [90, 92, 63, 91, 96, 63, 64], "new = old + 1", 13, 4, 3),
    Monkey(3, [65, 77], "new = old + 2", 3, 4, 6),
    Monkey(4, [76, 68, 94], "new = old * old", 2, 0, 6),
    Monkey(5, [86, 65, 66, 97, 73, 83], "new = old + 8", 11, 2, 3),
    Monkey(6, [78], "new = old + 6", 17, 0, 1),
    Monkey(7, [89, 57, 59, 61, 87, 55, 55, 88], "new = old + 7", 5, 2, 5),
]
div = 1
for i in [m.test for m in monkeys]:
    div *= i

for m in monkeys:
    m.set_div(div)

for round in range(10000):
    for monkey in monkeys:
        while monkey.has_items():
            target, item = monkey.inspect_2()
            monkeys[target].get_item(item)


res_2 = sorted([m.inspect_counter for m in monkeys])[-2:]
print("Part 1:", res_2[0] * res_2[1])
