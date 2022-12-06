"""
Advet of Code 2022
--- Day 5: Supply Stacks ---
"""

with open("input5", "r") as f:
    input = f.read()

stack, commands = input.split("\n\n")
stacks = {}

for line in stack.split("\n")[-2::-1]:
    for i, element in enumerate(line[1:-1:4]):
        index = i + 1
        if element == " ":
            continue
        if index not in stacks:
            stacks[index] = []
        stacks[index].append(element)


stacks_1 = stacks.copy()
stacks_2 = stacks.copy()


for line in commands.split("\n"):
    _, amount, _, origin, _, destination = line.strip().split(" ")
    amount, origin, destination = int(amount), int(origin), int(destination)
    stacks_2[origin], stacks_2[destination] = (
        stacks_2[origin][:-amount],
        stacks_2[destination] + stacks_2[origin][-amount:],
    )
    while amount > 0:
        curr = stacks_1[origin].pop()
        stacks_1[destination].append(curr)
        amount -= 1

print("Part 1:", "".join([x[-1] for x in stacks_1.values()]))
print("Part 2:", "".join([x[-1] for x in stacks_2.values()]))
